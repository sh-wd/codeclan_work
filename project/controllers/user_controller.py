from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from repositories import user_repsository
from repositories import transaction_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = user_repository.select_all() # NEW
    return render_template("books/index.html", all_books = books)