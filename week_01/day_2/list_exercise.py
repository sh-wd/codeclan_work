# 1. Create an empty list called `task_list`

# 2. Add a few `str` elements, representing some everyday tasks e.g. 'Make Dinner'

# 3. Print out `task_list`

# 4. Remove the last task

# 5. Print out `task_list`

# 6. Print out the number of elements in `task_list`

task_list = []
task_list.append("make dinner")
task_list.append("wash dishes")
print(task_list)

task_list.pop()
print(task_list)

lenght_of_tasks = len(task_list)
print(lenght_of_tasks)