from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def home():
    return "Hello, World!"

@freezer.register('/')
def frozen_home():
    return home()

if __name__ == '__main__':
    freezer.freeze()
