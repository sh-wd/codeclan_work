from db.run_sql import run_sql

from repositories import transaction_repository
from models.tag import Tag
  
def select_all():  
    tags = [] 

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        transaction_id = row['transaction_id']
        transaction = transaction_repository.select(transaction_id)
        tag = Tag(row['name'], transaction, row['id'] )
        tags.append(tag)
    return tags 

def save(tag):
    sql = "INSERT INTO tags (name, transaction_id) VALUES (%s, %s) RETURNING *"
    values = [tag.name, tag.transaction.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        transaction_id = result['transaction_id']
        transaction = transaction_repository.select(transaction_id)
        tag = Tag(result['name'], transaction, result['id'])
        return tag
    
def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET (name, transaction_id) = (%s, %s) WHERE id = %s"
    values = [tag.name, tag.transaction.id, tag.id]
    run_sql(sql, values)