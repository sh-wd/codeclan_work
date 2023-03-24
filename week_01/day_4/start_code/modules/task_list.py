
# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks = []

    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks
    

## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks = []

    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks
    

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    min_time_taken = []

    for task in list:
        if task["time_taken"] >= time:
            min_time_taken.append(task)
    return min_time_taken

## Find a task with a given description
def get_task_with_description(list, description):

    for task in list:
        if task["description"] == description:
           return task

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    task_status = []
    if status == "completed":
        boolean_status = True
    elif status == "incomplete":
        boolean_status = False
    else:
        print("invalid entry")
        return task_status

    for task in list:
        if task["completed"] == boolean_status:
            task_status.append(task)

    return task_status


