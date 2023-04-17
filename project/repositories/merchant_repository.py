from db.run_sql import run_sql

from repositories import transaction_repository
from models.merchant import Merchant
  
def select_all():  
    merchants = [] 

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        transaction_id = row['transaction_id']
        transaction = transaction_repository.select(transaction_id)
        merchant = Merchant(row['name'], transaction, row['id'] )
        merchants.append(merchant)
    return merchants 

def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING *"
    values = [merchant.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        transaction_id = result['transaction_id']
        transaction = transaction_repository.select(transaction_id)
        merchant = Merchant(result['name'], transaction, result['id'])
        return merchant
    
def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    sql = "UPDATE merchants SET (name, transaction_id) = (%s, %s) WHERE id = %s"
    values = [merchant.name, merchant.transaction.id, merchant.id]
    run_sql(sql, values)