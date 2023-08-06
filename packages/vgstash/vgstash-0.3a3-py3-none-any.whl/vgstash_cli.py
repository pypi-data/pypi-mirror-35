import vgstash
import sqlite3
import click
import sys

def get_db():
    """
    Convenience function to fetch a vgstash DB object from the default location.
    """
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
        click.echo("Added {} for {}. You {} it and {} it.{}".format(game.title, game.system, own_clause[game.ownership], progress_clause[game.progress], note_clause))
    except sqlite3.IntegrityError as e:
        print(e)
        click.echo("Couldn't add game.")


@cli.command('list')
@click.argument('filter', required=False)
def list_games(filter="allgames"):
    db = get_db()
    res = db.list_games(filter)
    for r in res:
        click.echo("{}|{}|{}|{}|{}".format(r['title'], r['system'], r['ownership'], r['progress'], r['notes']))
