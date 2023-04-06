from models.events import *

event_1 = Event('2023-04-9', 'Easter Dinner', '6', 'second floor', 'Classic easter sunday dinner', True)
event_2 = Event('2023-05-9', 'Barneys Wedding', '70', 'banquet hall', 'Barney and Daves wedding dinner', False)
event_3 = Event('2023-05-23', 'Leaving Party', '30', 'bar', 'Karen from finaces leaving drinks', False)

events = [event_1, event_2, event_3]

def add_new_event(event):
    events.append(event)

