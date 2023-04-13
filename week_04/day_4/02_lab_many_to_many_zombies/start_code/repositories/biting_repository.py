from db.run_sql import run_sql

from models.biting import Biting
from models.human import Human
from models.zombie import Zombie
from models.zombie_type import ZombieType

from repositories import human_repository, zombie_repository, zombie_type_repository

def save(biting):
    sql = "INSERT INTO bitings ( human_id, zombie_id, zombie_type) VALUES (%s, %s, %s) RETURNING id"
    values = (biting.human.id, biting.zombie.id, biting.zombie_type)
    results = run_sql(sql, values)
    biting.id = results[0]['id']
    return biting


def select_all():
    zombies = []

    sql = "SELECT * FROM zombies"
    results = run_sql(sql)
    
    for row in results:
        zombie = Zombie(row['name'], row['zombie_type'], row['id'])
        zombies.append(zombie)
    return zombies


def select(id):
    zombie = None
    sql = "SELECT * FROM zombies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        zombie = Zombie(result['name'], result['zombie_type'], result['id'])
    return zombie

def delete_all():
    sql = "DELETE FROM zombies"
    run_sql(sql)

def humans(zombie):
    humans = []
    sql = "SELECT humans.* FROM humans INNER JOIN bitings ON bitings.human_id = humans.id WHERE zombie_id = %s"
    values = zombie.id
    results = run_sql(sql, values)

    for row in results:
        human = Human(row['name'], row['id'])
        humans.append(human)

    return humans