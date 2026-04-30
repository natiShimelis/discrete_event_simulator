from queue import Queue
from server import Server
from event import Event, EventType

class Gateway:
    def __init__(self, queue, server):
        self.queue = queue
        self.server = server

    # Handles what happens when a message arrives at the Gateway
    def receive_message(self, message, current_time):
        # If the server is idle, send message straight to the server
        if not self.server.get_is_busy():
            self.server.set_is_busy(True)
            self.server.set_current_message(message)
            
            # Calculate when this message will finish processing
            service_time = self.server.get_service_time()
            departure_time = current_time + service_time
            
            # We must create and return the Departure event so the Engine can schedule it
            return Event(departure_time, EventType.MSG_DEPT, message)
        else:
            # If server is busy, put the message in the waiting queue
            self.queue.enqueue(message)
            return None 

    # Handles what happens when a message finishes processing
    def process_departure(self, current_time):
        # The current message leaves the system
        completed_message = self.server.get_current_message()
        self.server.set_current_message(None)
        self.server.set_is_busy(False)
        
        # Check if anyone is waiting in the queue
        if not self.queue.is_empty():
            # Pull the next message from the queue and send to server
            next_message = self.queue.dequeue()
            self.server.set_is_busy(True)
            self.server.set_current_message(next_message)
            
            # Calculate when this newly loaded message will finish
            service_time = self.server.get_service_time()
            departure_time = current_time + service_time
            
            # Return the Departure event for this next message
            return Event(departure_time, EventType.MSG_DEPT, next_message)
        
        return None # No one was waiting, server stays idle