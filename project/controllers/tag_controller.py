from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
from repositories import transaction_repository
from repositories import tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tags.select_all()
    return render_template("tags/index.html", tags=tags)