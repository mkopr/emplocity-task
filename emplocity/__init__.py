import os

from flask import Flask
from flask import render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.normpath(os.path.join(SRC_DIR, ".."))
BIN_DIR = os.path.join(ROOT_DIR, 'bin')

database = SQLAlchemy()


def get_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    from emplocity.models import FileData
    from emplocity.utils import add_to_database

    database.app = app
    database.init_app(app)
    database.create_all()

    add_to_database()

    admin = Admin(app, name='Admin console')
    admin.add_view(ModelView(FileData, database.session))

    @app.route('/')
    def index():
        return render_template(
            'index.html',
            file=FileData.query.all(),
        )

    @app.route('/<file_name>')
    def full_text(file_name):
        return render_template(
            'name.html',
            file=FileData.query.filter_by(name=file_name).all(),
        )

    app.run()
