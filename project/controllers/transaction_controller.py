from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from repositories import transaction_repository
from repositories import user_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)

@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    transactions = transaction_repository.select_all()
    return render_template("transactions/new.html", transactions=transactions)

# CREATE
# POST '/transactions'
@transactions_blueprint.route("/transactions",  methods=['POST'])
def create_transaction():
    cost = request.form['cost']
    user  = user_repository.select(request.form['user_id'])
    transaction = transaction(cost, user)
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
    users = user_repository.select_all()
    return render_template('transactions/edit.html', transaction=transaction, users=users)

# UPDATE
# PUT '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    cost = request.form['cost']
    user  = user_repository.select(request.form['user_id'])
    transaction = transaction(cost, id)
    print(transaction.user.name())
    transaction_repository.update(transaction)
    return redirect('/transactions')

# DELETE
# DELETE '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')