import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route('/')
def hello() -> str:
    return "Hello World"

@app.route('/<name>')
def hello_name(name: str) -> str:
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
