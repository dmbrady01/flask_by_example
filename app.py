import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Result

@app.route('/')
def hello() -> str:
    return "Hello World"

@app.route('/<name>')
def hello_name(name: str) -> str:
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
