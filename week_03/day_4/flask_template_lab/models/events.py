# from datetime import datetime

class Event():

    def __init__(self, date, event_name, guests, room_location, description, recurring):
        self.date = date
        self.event_name = event_name
        self.guests = guests
        self.room_location = room_location
        self.description = description
        self.recurring = recurring
