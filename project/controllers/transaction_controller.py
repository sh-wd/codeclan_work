from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from repositories import transaction_repository, merchant_repository, tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/users")
def users():
    return render_template("users/index.html")

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total_cost = transaction_repository.total_cost()
    return render_template("transactions/index.html", transactions=transactions, total_cost=total_cost)

@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    transactions = transaction_repository.select_all()
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", transactions=transactions, tags=tags, merchants=merchants)

# CREATE
# POST '/transactions'
@transactions_blueprint.route("/transactions",  methods=['POST'])
def create_transaction():
    cost = request.form['cost']
    cost_float = float(cost)
    cost_int = int(cost_float)
    merchant_id = request.form['merchants']
    merchant = merchant_repository.select(merchant_id)
    tag_id = request.form['tags']
    tag = tag_repository.select(tag_id)
    transaction = Transaction(cost_int, merchant, tag)

    transaction_repository.save(transaction)
    return redirect('/transactions')


# SHOW
# GET '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>", methods=['GET'])
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template('transactions/show.html', transaction=transaction)

# EDIT
# GET '/transactions/<id>/edit'
@transactions_blueprint.route("/transactions/<id>/edit", methods=['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template('transactions/edit.html', transaction=transaction)

# UPDATE
# PUT '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    cost = request.form['cost']
    merchant = request.form['merchant']
    tag = request.form['tag']
    transaction = Transaction(cost, merchant, tag, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')

# DELETE
# DELETE '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')