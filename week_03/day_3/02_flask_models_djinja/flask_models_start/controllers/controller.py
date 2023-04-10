from app import app
from flask import render_template
from models.todo_list import tasks

@app.route('/')
def index():
    return render_template('index.html', title='Home', tasks_var=tasks)

@app.route('/<int:id>')
def single_task(id):
    return render_template('show.html', title='Single Task', task=tasks[id])