from db.run_sql import run_sql

from models.transaction import Transaction

def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING *"
    values = user.name
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def get_transactions(user):
    transactions = []
    user_id = user.id
    sql = "SELECT * FROM transactions WHERE user_id = %s"
    values = [user_id]

    results = run_sql(sql, values)

    for row in results:
        transaction = Transaction(row['cost'], user, row['id'])
        transactions.append(transaction)

    return transactions

