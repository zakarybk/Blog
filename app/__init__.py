from flask import Flask, Blueprint, render_template

app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')
# Load the configuration from the instance folder
app.config.from_pyfile('config.py')
# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')

from .util import assets  # nopep8
# from . import views  # nopep8

from .home import home # nopep8
app.register_blueprint(home)