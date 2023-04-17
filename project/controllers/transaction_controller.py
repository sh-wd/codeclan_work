from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from repositories import transaction_repository
from repositories import user_repository
transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transactions.select_all()
    return render_template("transactions/index.html", transactions=transactions)