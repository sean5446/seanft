import os

from flask import Flask

template_dir = os.path.abspath(os.path.join(os.getcwd(), 'www'))
app = Flask(__name__, template_folder=template_dir)

with app.app_context():
    from . import routes

