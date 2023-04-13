from flask import Blueprint, render_template, request, redirect
from repositories import  task_repository, user_repository
from models.task import Task

tasks_blueprint = Blueprint("tasks",__name__)

# INDEX
# GET / tasks

@tasks_blueprint.route("/tasks")
def tasks():
    all_tasks = task_repository.select_all()
    return render_template("/tasks/index.html", all_tasks=all_tasks)

# NEW
# GET /tasks/new

@tasks_blueprint.route("/tasks/new")
def new_task():
    users  = user_repository.select_all()
    return render_template("tasks/new.html", all_users=users)

# CREATE
# POST /tasks
@tasks_blueprint.route("/tasks", methods=['POST'])
def create_tasks():
    description = request.form['description']
    user_id = request.form['user_id']
    durartion = request.form['duration']
    completed = request.form['completed']

    user = user_repository.select(user_id)
    task = Task(description, user, durartion, completed)
    task_repository.save(task)

    return redirect('/tasks')

# SHOW
# GET /tasks/<id>
@tasks_blueprint.route("/tasks/<id>")
def show_tasks(id):
    task = task_repository.select(id)
    return render_template("tasks/show.html", task=task)

# EDIT
# GET /tasks/<id>/edit
@tasks_blueprint.route("/tasks/<id>/edit")
def edit_task(id):
    task = task_repository.select(id)
    users = user_repository.select_all()
    return render_template("tasks/edit.html", task=task, all_users=users)

# UPDATE
# PUT (POST) /tasks/<id>
@tasks_blueprint.route("/tasks/<id>", methods=["POST"])
def update_task(id):
    description = request.form['description']
    user_id = request.form['user_id']
    durartion = request.form['duration']
    completed = request.form['completed']

    user = user_repository.select(user_id)
    task = Task(description, user, durartion, completed, id)
    task_repository.update(task)

    return redirect('/tasks')

# DELETE
# DELETE (POST) /task/<id>/delete

@tasks_blueprint.route("/tasks/<id>/delete", methods=["POST"])
def delete_tasks(id):
    task_repository.delete(id)
    return redirect('/tasks')