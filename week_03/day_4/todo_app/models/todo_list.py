from models.task import *



task1 = Task(1, "Buy groceries", "Milk, Cheese, Pizza, Fruit", False)
task2 = Task(2, "Learn Python", "Learn an awesome new programming language", True)
tasks = [task1, task2]

def find_task_by_id(id):
    for task in tasks:
        if task.id == id:
            return task
    return None

def add_new_task(task):
    tasks.append(task)