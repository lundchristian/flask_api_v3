import sqlite3
import click
from flask import current_app, g

class Database():
    def open():
        if 'db' not in g:
            g.db = sqlite3.connect(current_app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
            g.db.row_factory = sqlite3.Row
        return g.db

    def close(e=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    def initialize():
        db = Database.open()
        with current_app.open_resource('database/schema.sql') as sql_schema:
            db.executescript(sql_schema.read().decode('utf8'))

    @click.command('Database.initialize')
    def initialize_cli():
        Database.initialize()
        click.echo('Initialized the database.')

    def register(app):
        app.teardown_appcontext(Database.close)
        app.cli.add_command(Database.initialize_cli)