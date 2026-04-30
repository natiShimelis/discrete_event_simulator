import random

class Server:
    def __init__(self, server_id, mu_rate):
        self.server_id = str(server_id)
        self.mu_rate = mu_rate
        self.is_busy = False          # Tracks if the server is currently processing a message
        self.current_message = None   # Holds the message currently being processed

    # Getters
    def get_server_id(self):
        return self.server_id

    def get_mu_rate(self):
        return self.mu_rate

    def get_is_busy(self):
        return self.is_busy

    def get_current_message(self):
        return self.current_message

    # Setters
    def set_server_id(self, server_id):
        self.server_id = str(server_id)

    def set_mu_rate(self, mu_rate):
        self.mu_rate = mu_rate

    def set_is_busy(self, status):
        self.is_busy = status

    def set_current_message(self, message):
        self.current_message = message

    # Calculate the time it takes to process the current message
    def get_service_time(self):
        # random.expovariate uses mu as the rate
        # If mu_rate is 8 (per second), this returns times averaging 0.125 seconds
        return random.expovariate(self.mu_rate)

    # Print method for testing
    def print_server(self):
        status = "Busy" if self.is_busy else "Idle"
        print(f"Server ID: {self.server_id}, Mu Rate: {self.mu_rate} msgs/sec, Status: {status}")