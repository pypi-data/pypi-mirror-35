import vgstash
import sqlite3
import click
import sys

def get_db():
    """Fetch a vgstash DB object from the default location.

    Change DEFAULT_CONFIG['db_location'] before calling this function
    to alter behavior."""
    return vgstash.DB(vgstash.DEFAULT_CONFIG['db_location'])


@click.group('vgstash')
def cli():
    pass


@cli.command()
def init():
    db = get_db()
    click.echo("Initializing the database...")
    if db.create_schema():
        click.echo("Schema created.")
    else:
        raise sqlite3.OperationalError("Cannot create schema.")


@cli.command('add')
@click.argument('title', type=str)
@click.argument('system', type=str)
@click.argument('ownership', type=str, required=False, default=vgstash.DEFAULT_CONFIG['ownership'])
@click.argument('progress', type=str, required=False, default=vgstash.DEFAULT_CONFIG['progress'])
@click.argument('notes', type=str, required=False, default="")
def add(title, system, ownership, progress, notes):
    db = get_db()
    game = vgstash.Game(title, system, ownership, progress, notes)
    try:
        db.add_game(game, update=False)
        own_clause = (
            "do not own",
            "physically own",
            "digitally own",
            "digitally and physically own",
        )
        progress_clause = (
            "cannot beat",
            "haven't started",
            "are playing",
            "have beaten",
            "have completed",
        )
        note_clause = "" if len(game.notes) == 0 else " It also has notes."
        click.echo("Added {} for {}. You {} it and {} it.{}".format(
            game.title,
            game.system,
            own_clause[game.ownership],
            progress_clause[game.progress],
            note_clause,
        ))
    except sqlite3.IntegrityError as e:
        print(e)
        click.echo("Couldn't add game.")


@cli.command('list')
@click.argument('filter', required=False, default="allgames")
@click.option('--raw', '-r', is_flag=True, show_default=True, default=False, help="Output raw, pipe-delimited lines")
def list_games(filter, raw):
    db = get_db()
    res = db.list_games(filter)
    for r in res:
        if 'notes' in r.keys() and len(r['notes']) > 0:
            notes = r['notes'].replace('\n', '\\n')
            notes = notes.replace('\r', '\\r')
        else:
            notes = ''

        if raw:
            click.echo("|".join((
                r['title'],
                r['system'],
                str(r['ownership']),
                str(r['progress']),
                notes
            )
            ))
        else:
            pass
            #pretty_print(r)
