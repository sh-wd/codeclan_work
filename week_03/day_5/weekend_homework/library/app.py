from flask import Flask

app = Flask(__name__)

from contollers import controller

if __name__ == '__main__':
    app.run(debug=True)