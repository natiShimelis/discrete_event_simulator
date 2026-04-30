import random

class Server:
    def __init__(self, server_id, mu_rate):
        self.server_id = str(server_id)
        self.mu_rate = mu_rate
        self.is_busy = False
        self.current_message = None

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

    # Service Time
    def get_service_time(self):
        return random.expovariate(self.mu_rate)

    # Start Service
    def start_service(self, message):
        if self.is_busy:
            # x = "Server is currently busy"
            return None  # cannot serve
        self.current_message = message
        self.is_busy = True

        return self.get_service_time()

    # Finish Service
    def finish_service(self):
        finished_message = self.current_message

        self.current_message = None
        self.is_busy = False

        return finished_message

    # Print
    def print_server(self):
        status = "Busy" if self.is_busy else "Idle"
        print(f"Server ID: {self.server_id}, Mu Rate: {self.mu_rate}, Status: {status}")