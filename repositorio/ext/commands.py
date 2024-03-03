import click
from repositorio.model import db, tcc_artigo
from .authentication import create_user

def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        tcc_artigo(
            id=1, titulo="Ciabatta", autor="Willias",tipo="TCC", orientador="Raphael"
        ),
        tcc_artigo(id=2, name="Baguete", autor="Willias", tipo="TCC", orientador="Raphael"),
        tcc_artigo(id=3, name="Pretzel", autor="Willias", tipo="TCC", orientador="Raphael"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return tcc_artigo.query.all()


def init_app(app):
    
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
