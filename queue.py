class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    # Add message to queue
    def enqueue(self, message):
        if self.is_full():
            return False  # queue is full, message dropped
        self.queue.append(message)
        return True

    # Remove message from queue
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Check if queue is full
    def is_full(self):
        return len(self.queue) >= self.capacity

    # Get current size
    def get_size(self):
        return len(self.queue)

    # Debug print
    def print_queue(self):
        print("Queue contents:")
        for msg in self.queue:
            msg.print_message()