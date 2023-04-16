from db.run_sql import run_sql

from models.user import User
from models.transaction import Transaction
from repositories import transaction_repository
from repositories import merchant_repository
from repositories import tag_repository

def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING *"
    values = user.name
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():  
    users = [] 

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        transaction = transaction_repository.select(row['user_id'])
        user = User(row['name'], transaction, row['id'] )
        users.append(user)
    return users 

def get_transactions(user):
    transactions = []
    user_id = user.id
    sql = "SELECT * FROM transactions WHERE user_id = %s"
    values = [user_id]

    results = run_sql(sql, values)

    for row in results:
        transaction = Transaction(row['cost'], row['id'])
        transactions.append(transaction)

    return transactions

