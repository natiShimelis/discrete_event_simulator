class Message:
    _id_counter = 1  # class variable

    def __init__(self, source, destination):
        self.message_id = Message._id_counter
        Message._id_counter += 1

        self.source = source
        self.destination = destination

    # Getters
    def get_message_id(self):
        return self.message_id

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    # Setters
    def set_source(self, source):
        self.source = source

    def set_destination(self, destination):
        self.destination = destination

    # Print method
    def print_message(self):
        print(f"Message ID: {self.message_id}, Source: {self.source}, Destination: {self.destination}")