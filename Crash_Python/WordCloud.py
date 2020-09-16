# Problem Statement

# The manager wants to create a daily report that tracks the use of machines, It is you job to create


# Inputs - list of  Events
# Objective - We need to process a list of Event objects using their attributes to generate a report that lists all users currently logged in to the machines.
# Outputs - create a report that lists all the machine namses and for each machine, list of the users that are currently logged in
# Event class, Contains the date when the event happened, the name of the machine where it happened, the user involved, and the event type
# Atributes date, user, machine, type, The event type are string and we need to be care about are login and logout
# Need to process the events for to generate a report - Sor the list of events cronologically - Store the data in a dictionary of sets,
# which we will use for to track of who is loged
# Need to functions for create and print the dictionary

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
