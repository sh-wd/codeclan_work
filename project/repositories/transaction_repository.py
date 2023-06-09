from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

from repositories import merchant_repository
from repositories import tag_repository
import pdb

def get_merchants(transaction):
    merchants = []
    transaction_id = transaction.id
    sql = "SELECT * FROM merchants WHERE transaction_id = %s"
    values = [transaction_id]

    results = run_sql(sql, values)

    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)

    return merchants

def get_tags(transaction):
    tags = []
    transaction_id = transaction.id
    sql = "SELECT * FROM merchants WHERE transaction_id = %s"
    values = [transaction_id]

    results = run_sql(sql, values)

    for row in results:
        tag = Tag(row['name'], row['id'])
        tags.append(tag)

    return tags

def save(transaction):
    sql = "INSERT INTO transactions (cost, merchant_id, tag_id) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.cost, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def select_all():  
    transactions = [] 

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
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
        merchant = merchant_repository.select(result['merchant_id'])
        tag = tag_repository.select(result['tag_id'])
        transaction = Transaction(result['cost'], merchant, tag, result['id'] )
        return transaction
    
def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (cost, merchant_id, tag_id) = (%s, %s, %s) WHERE id = %s"
    values = [transaction.cost, transaction.merchant.id, transaction.tag.id, transaction.id]
    run_sql(sql, values)

def total_cost():
    sql = "SELECT SUM(cost) FROM transactions;"
    result = run_sql(sql)
    return result[0][0]