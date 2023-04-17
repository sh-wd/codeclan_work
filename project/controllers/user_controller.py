from flask import Flask, render_template
from flask import Blueprint
from models.transaction import Transaction
from repositories import user_repository
from repositories import transaction_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users=users)
