import random
from message import Message

class Client:
    def __init__(self, client_id, lambda_rate):
        self.client_id = str(client_id)
        self.lambda_rate = lambda_rate

    # Getters
    def get_client_id(self):
        return self.client_id

    def get_lambda_rate(self):
        return self.lambda_rate

    # Setters
    def set_client_id(self, client_id):
        self.client_id = str(client_id)

    def set_lambda_rate(self, lambda_rate):
        self.lambda_rate = lambda_rate

    # Generate a new Message object
    def create_message(self, destination):
        # The client acts as the source
        return Message(self.client_id, str(destination))

    # Calculate the time delay until the next message is generated
    def get_next_arrival_time(self):
        # random.expovariate uses lambda as the rate
        # If lambda_rate is 4 (per second), this will return times averaging 0.25 seconds
        return random.expovariate(self.lambda_rate)

    # Print method for testing
    def print_client(self):
        print(f"Client ID: {self.client_id}, Lambda Rate: {self.lambda_rate} msgs/sec")