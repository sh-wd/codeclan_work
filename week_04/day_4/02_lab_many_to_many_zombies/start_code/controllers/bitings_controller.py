from flask import Blueprint, Flask, redirect, render_template, request
import repositories.biting_repository as biting_repository
import repositories.human_repository as human_repository
import repositories.zombie_repository as zombie_repository
import repositories.zombie_type_repository as zombie_type_repository
from models.biting import Biting

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", biting = bitings)
# NEW
@bitings_blueprint.route("/bitings/new", methods=["GET"])
def new_bite():
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template("bitings/new.html", humans = humans, zombies = zombies)

# CREATE
@bitings_blueprint.route("/bitings", methods = ["POST"])
def create_bite():
    human_id = request.form['human_id']
    zombie_id = request.form['zombie_id']
    zombie_type = request.form['zombie_type']
    human = human_repository.select(human_id)
    zombie = zombie_repository.select(zombie_id)
    biting = Biting(human, zombie, zombie_type)
    biting_repository.save(biting)
    return redirect('/bitings')

# EDIT
@bitings_blueprint.route("/bitings/<id>/edit")
def edit_biting(id):
    biting = biting_repository.select(id)
    zombie = zombie_repository.select(id)
    human = human_repository.select(id)
    return render_template('bitings/edit.html', biting=biting, zombie=zombie, human=human)



# UPDATE

# DELETE

@bitings_blueprint.route("/bitings/<id>/delete", methods = ['POST'])
def delete_bite(id):
    biting_repository.delete(id)
    return redirect('/bitings')
