from time import sleep

def singleton(cls):
    return cls()

@singleton
class EventManager:
    def __init__(self):
        self.events = []
    def add_event(self, event):
        self.events.append(event)
    def print_events(self):
        print("Events : {}".format(self.events))

sleep(10000)

