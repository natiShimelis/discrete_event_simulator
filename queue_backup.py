class Queue:
    def __init__(self):
        self.messages = []  # List to act as our FIFO queue

    # Add a message to the back of the queue
    def enqueue(self, message):
        self.messages.append(message)

    # Remove and return a message from the front of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.messages.pop(0)
        return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self.messages) == 0

    # Get the current number of messages waiting
    def get_size(self):
        return len(self.messages)

    # Print method for testing (matches the style of your other classes)
    def print_queue(self):
        print(f"Queue currently has {self.get_size()} message(s):")
        for msg in self.messages:
            msg.print_message()