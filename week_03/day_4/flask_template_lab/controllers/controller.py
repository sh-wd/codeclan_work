from app import app
from flask import render_template, request
from models.events_list import events, add_new_event
from models.events import Event

@app.route('/events')
def index():
    return render_template('index.html', events_list=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name']
    no_of_guests = request.form['guests']
    room_location = request.form['room_location']
    description = request.form['description']
    recurring = request.form['recurring'] == "yes"
    new_event = Event(event_date, event_name, no_of_guests, room_location, description, recurring)
    add_new_event(new_event)

    return render_template('index.html', events_list = events)