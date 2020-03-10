from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return "Hello World"

@app.route('/<name>')
def hello_name(name: str) -> str:
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
