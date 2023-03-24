from data.task_list import *
from modules.task_list import *
from modules.output import *

def option_4():

    option == '4':
        description = input("Enter task description to search for: ")
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")