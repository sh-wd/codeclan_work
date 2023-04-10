from flask import Flask

app = Flask(__name__)

from contollers import task_controller

if __name__ == "__main__":
    app.run(debug=True)

