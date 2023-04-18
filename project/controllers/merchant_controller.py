from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import merchant_repository
from models.merchant import Merchant

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants=merchants)

@merchants_blueprint.route("/merchants/new", methods=['GET'])
def new_merchant():
    merchants = merchant_repository.select_all()
    return render_template("merchants/new.html", merchants=merchants)

# CREATE
# POST '/merchants'
@merchants_blueprint.route("/merchants",  methods=['POST'])
def create_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect('/merchants')


# SHOW
# GET '/merchants/<id>'
@merchants_blueprint.route("/merchants/<id>", methods=['GET'])
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/show.html', merchant=merchant)

# EDIT
# GET '/merchants/<id>/edit'
@merchants_blueprint.route("/merchants/<id>/edit", methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant=merchant)

# UPDATE
# PUT '/merchants/<id>'
@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    name = request.form['name']
    merchant = Merchant(name, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')

# DELETE
# DELETE '/merchants/<id>'
@merchants_blueprint.route("/merchants/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect('/merchants')