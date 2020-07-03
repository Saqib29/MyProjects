## # A simple Python Project (Users loggedin/loggedout reports generating)

The problem is to get a report on everyday activities of the users. Finding which user login to which machine & when logged in when logged out. Writting the script on `Python` for this problem to get a report on everyday users.

```python

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

def get_event_date(event):
    return event.date

def current_users(events): # here events is the list of instances of Event Class
    events.sort(key=get_event_date)  # we will sort the events according to the time where "get_event_date" func used in the sort method
    machines = {}
    for event in events:  # every instances goes to the event from the events list
        if event.machine not in machines:
            machines[event.machine] = set() # if the machine is not exist in the dictionary it will create a new pair, where set() as value
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            if event.user in machines[event.machine]:
                machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
generate_report(users)


```

> - **Event** is a class where **event** is an instance of `Event` class
> - The `Event` class contains `date(when the event happened)`, `name of machine(where it happened on which machine?)`, `user(which user occured the event)` & `type of event(login/logout)`
    
- Attributes are:-
    - Date
    - User
    - Machine
    - Type -- string(login/logout)