import pdb 
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository  
from repositories import user_repository

task_repository.delete_all()
user_repository.delete_all()

user_1 = User('Scooby', 'Doo')
user_repository.save(user_1)

user_2 = User('Scrappy', 'Doo')
user_repository.save(user_2)

task = Task("Walk dog", user_1, 40)
task_repository.save(task)

task_2 = Task("Walk dog some more", user_2, 45)
task_repository.save(task_2)

results = user_repository.get_tasks(user_1)

for result in results:
    print(f"{result.__dict__} : {result.user.first_name}")

# result = task_repository.select_all()

# for task in result:
#     print(task.__dict__)


# users = user_repository.select_all()

# for user in users:
#     print(user.__dict__)

# task_1 = Task("Go for a run", "Jack Jarvis", 20)

# task_repository.save(task_1)

# task_1.mark_complete()
# task_repository.update(task_1)


# pdb.set_trace()