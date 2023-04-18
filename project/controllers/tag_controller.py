from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
from repositories import tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags=tags)

@tags_blueprint.route("/tags/new", methods=['GET'])
def new_tag():
    tags = tag_repository.select_all()
    return render_template("tags/new.html", tags=tags)

# CREATE
# POST '/tags'
@tags_blueprint.route("/tags",  methods=['POST'])
def create_tag():
    name = request.form['name']
    tag = Tag(name)
    tag_repository.save(tag)
    return redirect('/tags')


# SHOW
# GET '/tags/<id>'
@tags_blueprint.route("/tags/<id>", methods=['GET'])
def show_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/show.html', tag=tag)

# EDIT
# GET '/tags/<id>/edit'
@tags_blueprint.route("/tags/<id>/edit", methods=['GET'])
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag=tag)

# UPDATE
# PUT '/tags/<id>'
@tags_blueprint.route("/tags/<id>", methods=['POST'])
def update_tag(id):
    name = request.form['name']
    tag = Tag(name, id)
    tag_repository.update(tag)
    return redirect('/tags')

# DELETE
# DELETE '/tags/<id>'
@tags_blueprint.route("/tags/<id>/delete", methods=['POST'])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect('/tags')