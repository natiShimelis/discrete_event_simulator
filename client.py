import random
from message import Message
from event import Event, EventType


class Client:
    def __init__(self, client_id, lambda_rate):
        self.client_id = str(client_id)
        self.lambda_rate = lambda_rate

    # Generate inter-arrival time
    def generate_interarrival_time(self):
        return random.expovariate(self.lambda_rate)

    # We create and schedule a SEND event
    def send_message(self, current_time, scheduler):
        # Time for next message
        interarrival = self.generate_interarrival_time()
        event_time = current_time + interarrival

        # Create message
        message = Message(source=self.client_id, destination="0")

        # Create event
        event = Event(event_time, EventType.SEND_MSG, message)

        # We add it to scheduler
        scheduler.add_event(event)

        return event

    # Print 
    def print_client(self):
        print(f"Client ID: {self.client_id}, Lambda: {self.lambda_rate}")