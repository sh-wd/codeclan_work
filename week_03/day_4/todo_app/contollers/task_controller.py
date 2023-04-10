from app import app
from flask import render_template, request, redirect, url_for
from models.todo_list import tasks, find_task_by_id, add_new_task
from models.task import Task

@app.errorhandler(404)
def display_404(err):
    return render_template('404.html')

@app.route('/')
def index():
    return redirect(url_for('all_tasks'))

@app.route('/tasks')
def all_tasks():
    return render_template('index.html', task_list=tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task_title = request.form['title']
    task_description = request.form['description']
    new_id = len(tasks) + 1
    new_task = Task(new_id, task_title, task_description, False)
    add_new_task(new_task)
    return render_template('index.html', task_list=tasks)

@app.route('/tasks/<int:task_id>')
def show_task(task_id):
    task = find_task_by_id(task_id)
    return render_template('show.html', task=task)

    