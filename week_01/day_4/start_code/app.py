from modules.output import *
from modules.task_list import *
from data.task_list import *

while (True):
    print_menu()
    option = input("Select an option 1, 2, 3, 4, 5, 6, 7, 8 display (m)enu or (q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif 
    elif option == '5':
        time = int(input("Enter task duration: "))
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        description = input("Enter task description to search for: ")
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = create_task(description, time_taken)
        tasks.append(task)
    elif option == '8':
        status = input("What status of tasks would you like? ")
        print_list(get_tasks_by_status(tasks, status))
    else:
        print("Invalid Input - choose another option")
