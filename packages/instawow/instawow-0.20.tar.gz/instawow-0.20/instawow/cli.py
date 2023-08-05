
from collections import namedtuple
from functools import partial, reduce
from textwrap import fill
import traceback
import typing as T
import webbrowser

import click
from outdated import check_outdated
from sqlalchemy import inspect, text
from texttable import Texttable

from . import __version__
from .config import UserConfig
from .manager import CliManager as Manager
from .models import Pkg, PkgFolder
from .utils import TocReader, slugify


_SUCCESS = click.style('✓', fg='green')
_FAILURE = click.style('✗', fg='red')

MESSAGES = {
    Manager.PkgInstalled:
        f'{_SUCCESS} {{0}}: installed {{1.new_pkg.version}}'
        f' from {{1.new_pkg.options.strategy}}'.format,
    Manager.PkgUpdated:
        f'{_SUCCESS} {{0}}: updated {{1.old_pkg.version}} to {{1.new_pkg.version}}'
        f' from {{1.new_pkg.options.strategy}}'.format,
    Manager.PkgRemoved:
        f'{_SUCCESS} {{}}: removed'.format,
    Manager.PkgAlreadyInstalled:
        f'{_FAILURE} {{}}: already installed'.format,
    Manager.PkgConflictsWithInstalled:
        lambda a, r: f'{_FAILURE} {a}: conflicts with installed '
                     f'add-on {_compose_addon_defn(r.conflicting_pkg)}',
    Manager.PkgConflictsWithPreexisting:
        f'{_FAILURE} {{}}: conflicts with an add-on not installed by instawow\n'
         '  pass `-o` to `install` if you do actually wish to overwrite this add-on'
        .format,
    Manager.PkgNonexistent:
        f'{_FAILURE} {{}}: no such project id or slug'.format,
    Manager.PkgNotInstalled:
        f'{_FAILURE} {{}}: not installed'.format,
    Manager.PkgOriginInvalid:
        f'{_FAILURE} {{}}: invalid origin'.format,
    Manager.PkgUpToDate:   # IGNORE
        ...,
    Manager.InternalError:
        lambda _, r: ''.join(traceback.format_exception(r.error.__class__,
                                                        r.error,
                                                        r.error.__traceback__)).rstrip(),}

_CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}
_SEP = ':'

_parts = namedtuple('Parts', 'origin id_or_slug')


def _format_message(addon, result):
    return MESSAGES[result if isinstance(result, type)
                    else result.__class__](addon, result)


def _tabulate(rows: T.List[T.Tuple[str, ...]], *,
              head: T.Tuple[str, ...]=(), show_index: bool=True) -> str:
    table = Texttable(max_width=0)
    table.set_deco(Texttable.VLINES | Texttable.BORDER |
                   Texttable.HEADER)

    if show_index:
        table.set_cols_align(('r', *('l' for _ in rows[0])))
        head = ('', *head)
        rows = [(i, *v) for i, v in enumerate(rows, start=1)]
    table.add_rows([head, *rows])
    return table.draw()


def _compose_addon_defn(val):
    try:
        origin, slug = val.origin, val.slug
    except AttributeError:
        origin, slug = val
    return _SEP.join((origin, slug))


def _decompose_addon_defn(ctx, param, value, *,
                          raise_for_invalid_defn=True):
    if isinstance(value, tuple):
        return tuple(_decompose_addon_defn(ctx, param, v)
                     for v in sorted(set(value), key=value.index))

    for resolver in ctx.obj.resolvers.values():
        parts = resolver.decompose_url(value)
        if parts:
            parts = _parts(*parts)
            break
    else:
        if _SEP not in value:
            if raise_for_invalid_defn:
                raise click.BadParameter(value)
            parts = _parts('*', value)
        else:
            parts = value.partition(_SEP)
            parts = _parts(parts[0], slugify(parts[2]))
    return _compose_addon_defn(parts), parts


class _OrigCmdOrderGroup(click.Group):

    def list_commands(self, ctx):
        return self.commands    # The default is ``sorted(self.commands)``


def _init():
    addon_dir = UserConfig.detect_addon_dir()
    while True:
        try:
            UserConfig(addon_dir=addon_dir).write()
        except ValueError:
            if addon_dir:
                click.echo(f'{addon_dir} not found')
            addon_dir = click.prompt('Enter the path to your add-on folder')
        else:
            break

init = click.Command(name='instawow-init', callback=_init,
                     context_settings=_CONTEXT_SETTINGS)


@click.group(cls=_OrigCmdOrderGroup, context_settings=_CONTEXT_SETTINGS)
@click.version_option(__version__)
@click.option('--hide-progress', '-n', is_flag=True, default=False,
              help='Hide the progress bar.')
@click.pass_context
def main(ctx, hide_progress):
    """Add-on manager for World of Warcraft."""
    if not ctx.obj:
        while True:
            try:
                config = UserConfig.read()
            except (FileNotFoundError, ValueError):
                _init()
            else:
                break
        ctx.obj = Manager(config=config,
                          show_progress=not hide_progress)

        is_outdated, _latest_version = check_outdated('instawow',
                                                      __version__)
        if is_outdated:
            click.echo(f'{click.style("!", fg="blue")} instawow is out of date:\n'
                       f'  run `python3 -m pip install -U instawow` to upgrade')

cli = main


@main.command()
@click.argument('addons', nargs=-1, required=True, callback=_decompose_addon_defn)
@click.option('--strategy', '-s',
              type=click.Choice(['canonical', 'latest']),
              default='canonical',
              help="Whether to install the latest published version "
                   "('canonical') or the very latest upload ('latest').")
@click.option('--overwrite', '-o',
              is_flag=True, default=False,
              help='Overwrite existing add-ons.')
@click.pass_obj
def install(manager, addons, overwrite, strategy):
    """Install add-ons."""
    for addon, result in zip((d for d, _ in addons),
                             manager.install_many((*p, strategy, overwrite)
                                                  for _, p in addons)):
        click.echo(_format_message(addon, result))


@main.command()
@click.argument('addons', nargs=-1, callback=_decompose_addon_defn)
@click.option('--strategy', '-s',
              type=click.Choice(['canonical', 'latest']), default=None,
              help="Whether to update to the latest published version "
                   "('canonical') or the very latest upload ('latest').")
@click.pass_obj
def update(manager, addons, strategy):
    """Update installed add-ons."""
    if not addons:
        addons = [(_compose_addon_defn(p), (p.origin, p.slug))
                  for p in manager.db.query(Pkg).all()]
    if strategy:
        for pkg in (manager.get(*p) for _, p in addons):
            pkg.options.strategy = strategy
        manager.db.commit()

    for addon, result in zip((d for d, _ in addons),
                             manager.update_many(p for _, p in addons)):
        if not isinstance(result, Manager.PkgUpToDate):
            click.echo(_format_message(addon, result))


@main.command()
@click.argument('addons', nargs=-1, required=True, callback=_decompose_addon_defn)
@click.pass_obj
def remove(manager, addons):
    """Uninstall add-ons."""
    for addon, parts in addons:
        try:
            result = manager.remove(*parts)
        except (Manager.ManagerError, Manager.InternalError) as error:
            result = error
        click.echo(_format_message(addon, result))


@main.group('list')
def list_():
    """List add-ons."""


@list_.command('installed')
@click.option('--column', '-c', 'columns',
              multiple=True,
              help='A field to show in a column.  Nested fields are '
                   'dot-delimited.  Repeatable.')
@click.option('--columns', '-C', 'print_columns',
              is_flag=True, default=False,
              help='Print a list of all possible column values.')
@click.option('--toc-entry', '-t', 'toc_entries',
              multiple=True,
              help='An entry to extract from the TOC.  Repeatable.')
@click.option('--sort-by', '-s', 'sort_key',
              default='name',
              help='A key to sort the table by.  '
                   'You can chain multiple keys by separating them with a comma '
                   'just as you would in SQL, '
                   'e.g. `--sort-by="origin, date_published DESC"`.')
@click.pass_obj
def list_installed(manager,
                   columns, print_columns, toc_entries,
                   sort_key):
    """List installed add-ons."""
    def format_columns(pkg):
        for column in columns:
            try:
                value = reduce(getattr, [pkg] + column.split('.'))
            except AttributeError:
                raise click.BadParameter(column,
                                         param_hint=['--column', '-c'])
            if column == 'folders':
                value = '\n'.join(f.path.name for f in value)
            elif column == 'options':
                value = {'strategy': value.strategy}
            elif column == 'description':
                value = fill(value, width=50, max_lines=3)
            yield value

    def format_toc_entries(pkg):
        toc_readers = [TocReader(f.path/f'{f.path.name}.toc')
                       for f in pkg.folders]
        for toc_entry in toc_entries:
            value = [fill(r[toc_entry].value or '', width=50)
                     for r in toc_readers]
            value = sorted(set(value), key=value.index)
            value = '\n'.join(value)
            yield value

    if print_columns:
        click.echo(_tabulate([(c,) for c in (*inspect(Pkg).columns.keys(),
                                             *inspect(Pkg).relationships.keys())],
                             head=('field',), show_index=False))
    else:
        click.echo(_tabulate([(_compose_addon_defn(p),
                               *format_columns(p),
                               *format_toc_entries(p))
                              for p in manager.db.query(Pkg)
                                                 .order_by(text(sort_key))
                                                 .all()],
                             head=('add-on',
                                   *columns,
                                   *(f'[{e}]' for e in toc_entries))))


@list_.command('outdated')
@click.option('--flip', '-f', 'should_flip',
              is_flag=True, help='Check against the opposing strategy.')
@click.pass_obj
def list_outdated(manager, should_flip):
    """List outdated add-ons."""
    def flip(strategy):
        if should_flip:
            strategy = 'latest' if strategy == 'canonical' else 'canonical'
        return strategy

    outdated = manager.db.query(Pkg).order_by(Pkg.name).all()
    outdated = zip(outdated, manager.resolve_many((p.origin, p.id,
                                                   flip(p.options.strategy))
                                                  for p in outdated))
    outdated = [(i, n) for i, n in outdated if i.file_id != n.file_id]
    if outdated:
        click.echo(_tabulate([(_compose_addon_defn(n),
                               i.version, n.version, n.options.strategy)
                              for i, n in outdated],
                             head=('add-on', 'installed', 'new', 'strategy')))


@list_.command('preexisting')
@click.pass_obj
def list_preexisting(manager):
    """List add-ons not installed by instawow."""
    folders = {f.name
               for f in manager.config.addon_dir.iterdir() if f.is_dir()} - \
              {f.path.name for f in manager.db.query(PkgFolder).all()}
    folders = ((n, manager.config.addon_dir/n/f'{n}.toc') for n in folders)
    folders = {(n, TocReader(t)) for n, t in folders if t.exists()}
    if folders:
        click.echo(_tabulate([(n,
                               t['X-Curse-Project-ID'].value or '',
                               t['X-WoWI-ID'].value or '',
                               t['X-Curse-Packaged-Version', 'X-Packaged-Version',
                                 'Version'].value or '')
                              for n, t in sorted(folders)],
                             head=('folder', 'Curse ID', 'WoWI ID', 'version')))


@main.command()
@click.argument('addon', callback=partial(_decompose_addon_defn,
                                          raise_for_invalid_defn=False))
@click.option('--toc-entry', '-t', 'toc_entries',
              multiple=True,
              help='An entry to extract from the TOC.  Repeatable.')
@click.pass_obj
def info(manager, addon, toc_entries):
    """Show the details of an installed add-on."""
    pkg = addon[1]
    pkg = (manager.get(*pkg) or manager.db.query(Pkg)
                                          .filter(Pkg.slug.contains(pkg.id_or_slug))
                                          .order_by(Pkg.name)
                                          .first())
    if pkg:
        rows = {'name': pkg.name,
                'source': pkg.origin,
                'id': pkg.id,
                'slug': pkg.slug,
                'description': fill(pkg.description, max_lines=5),
                'homepage': pkg.url,
                'version': pkg.version,
                'release date': pkg.date_published,
                'folders': '\n'.join([str(pkg.folders[0].path.parent)] +
                                     [' ├─ ' + f.path.name for f in pkg.folders[:-1]] +
                                     [' └─ ' + pkg.folders[-1].path.name]),
                'strategy': pkg.options.strategy,}

        if toc_entries:
            for path, toc_reader in ((f.path,
                                      TocReader(f.path/f'{f.path.name}.toc'))
                                     for f in pkg.folders):
                rows.update({f'[{path.name} {k}]': fill(toc_reader[k].value or '')
                             for k in toc_entries})
        click.echo(_tabulate(rows.items(), show_index=False))
    else:
        click.echo(_format_message(addon[0], Manager.PkgNotInstalled))


@main.command()
@click.argument('addon', callback=partial(_decompose_addon_defn,
                                          raise_for_invalid_defn=False))
@click.pass_obj
def hearth(manager, addon):
    """Open the add-on's homepage in your browser."""
    pkg = addon[1]
    pkg = (manager.get(*pkg) or manager.db.query(Pkg)
                                          .filter(Pkg.slug.contains(pkg.id_or_slug))
                                          .order_by(Pkg.name)
                                          .first())
    if pkg:
        webbrowser.open(pkg.url)
    else:
        click.echo(_format_message(addon[0], Manager.PkgNotInstalled))


@main.command()
@click.argument('addon', callback=partial(_decompose_addon_defn,
                                          raise_for_invalid_defn=False))
@click.pass_obj
def reveal(manager, addon):
    """Open the add-on folder in your file manager."""
    pkg = addon[1]
    pkg = (manager.get(*pkg) or manager.db.query(Pkg)
                                          .filter(Pkg.slug.contains(pkg.id_or_slug))
                                          .order_by(Pkg.name)
                                          .first())
    if pkg:
        webbrowser.open(pkg.folders[0].path.as_uri())
    else:
        click.echo(_format_message(addon[0], Manager.PkgNotInstalled))


@main.group()
def extras():
    """Additional functionality."""


@extras.group()
def bitbar():
    """Mini update GUI implemented as a BitBar plug-in.

    BitBar <https://getbitbar.com/> is a menu-bar app host for macOS.
    """


@bitbar.command('_generate')
@click.argument('caller')
@click.argument('version')
@click.pass_obj
def bitbar_generate(manager, caller, version):
    from base64 import b64encode
    from pathlib import Path
    from subprocess import run, PIPE

    outdated = manager.db.query(Pkg).order_by(Pkg.name).all()
    outdated = zip(outdated,
                   manager.resolve_many((p.origin, p.id, p.options.strategy)
                                        for p in outdated))
    outdated = [(p, r) for p, r in outdated
                if p.file_id != getattr(r, 'file_id', p.file_id)]

    icon = Path(__file__).parent/'assets'/f'''\
NSStatusItem-icon__\
{"has-updates" if outdated else "clear"}\
{"@2x" if b"Retina" in run(("system_profiler", "SPDisplaysDataType"),
                           stdout=PIPE).stdout else ""}\
.png'''
    icon = b64encode(icon.read_bytes()).decode()

    click.echo(f'''| templateImage="{icon}"
---
instawow ({__version__}:{version})''')
    if outdated:
        if len(outdated) > 1:
            click.echo(f'''\
Update all | bash={caller} param1=update terminal=false refresh=true''')
        for p, r in outdated:
            click.echo(f'''\
Update “{r.name}” ({p.version} ➞ {r.version}) | \
  refresh=true \
  bash={caller} param1=update param2={_compose_addon_defn(r)} terminal=false
View “{r.name}” on {manager.resolvers[r.origin].name} | \
  alternate=true \
  bash={caller} param1=hearth param2={_compose_addon_defn(r)} terminal=false''')


@bitbar.command('install')
def bitbar_install():
    """Install the instawow BitBar plug-in."""
    from pathlib import Path
    import tempfile
    import sys

    with tempfile.TemporaryDirectory() as name:
        path = Path(name, 'instawow.1h.py')
        path.write_text(f'''\
#!/usr/bin/env LC_ALL=en_US.UTF-8 {sys.executable}

__version__ = {__version__!r}

import sys

from instawow.cli import main

main(['-n', *(sys.argv[1:] or ['extras', 'bitbar', '_generate', sys.argv[0], __version__])])
''')
        webbrowser.open(f'bitbar://openPlugin?src={path.as_uri()}')
        click.pause('Press any key to exit after installing the plug-in')
