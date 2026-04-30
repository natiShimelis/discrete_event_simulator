class Scheduler:
    def __init__(self):
        self.events = []  # list to store events

    # Add event in sorted order (by event_time)
    def add_event(self, event):
        if not self.events:
            self.events.append(event)
            return

        inserted = False

        for i in range(len(self.events)):
            if event.get_event_time() < self.events[i].get_event_time():
                self.events.insert(i, event)
                inserted = True
                break

        if not inserted:
            self.events.append(event)

    # Get the next event (smallest time)
    def get_event(self):
        if self.events:
            return self.events.pop(0)
        return None

    # Peek current time (time of next event)
    def get_current_time(self):
        if self.events:
            return self.events[0].get_event_time()
        return None

    # Check if empty
    def is_empty(self):
        return len(self.events) == 0

    # Print all events (for debugging)
    def print_events(self):
        print("Scheduled Events:")
        for event in self.events:
            event.print_event()