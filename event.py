from enum import Enum

class EventType(Enum):
    SEND_MSG = "SEND"
    RECV_MSG = "RECV"
    MSG_DEPT = "DEPT"


class Event:
    def __init__(self, event_time, event_type, message):
        self.event_time = event_time
        self.event_type = event_type
        self.message = message

    # Getters
    def get_event_time(self):
        return self.event_time

    def get_event_type(self):
        return self.event_type

    def get_message(self):
        return self.message

    # Setters
    def set_event_time(self, event_time):
        self.event_time = event_time

    def set_event_type(self, event_type):
        self.event_type = event_type

    # Print method
    def print_event(self):
        print(f"Time: {self.event_time}, Type: {self.event_type.value}")
        self.message.print_message()