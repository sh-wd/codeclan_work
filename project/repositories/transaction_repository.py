from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

from repositories import merchant_repository
from repositories import tag_repository

def get_merchants(transaction):
    merchants = []
    transaction_id = transaction.id
    sql = "SELECT * FROM merchants WHERE transaction_id = %s"
    values = [transaction_id]

    results = run_sql(sql, values)

    for row in results:
        merchant = Merchant(row['name'], transaction, row['id'])
        merchants.append(merchant)

    return merchants

def get_tags(transaction):
    tags = []
    transaction_id = transaction.id
    sql = "SELECT * FROM merchants WHERE transaction_id = %s"
    values = [transaction_id]

    results = run_sql(sql, values)

    for row in results:
        tag = Tag(row['name'], transaction, row['id'])
        tags.append(tag)

    return tags

def save(transaction, merchant, tag):
    sql = "INSERT INTO transactions (cost, merchant_name, tag_name) VALUES (%s, %s, %s) RETURNING *"
    values = [transaction.cost, merchant.name, tag.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def select_all():  
    transactions = [] 

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(results['transaction_id'])
        tag = tag_repository.select(results['transaction_id'])
        transaction = Transaction(row['cost'], merchant, tag, row['id'] )
        transactions.append(transaction)
    return transactions 

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        transaction = Transaction(result['cost'], result['id'])
        return transaction
    
def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET cost = %s WHERE id = %s"
    values = [transaction.cost, transaction.id]
    run_sql(sql, values)