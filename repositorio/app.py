from flask import Flask 
from .ext import authentication, configuration, database, commands, admin
from .view import init_app


def create_app():
   app = Flask(__name__)
   configuration.init_app(app)
   database.init_app(app)
   commands.init_app(app)
   init_app(app)
   authentication.init_app(app)
   admin.init_app(app)
   return app