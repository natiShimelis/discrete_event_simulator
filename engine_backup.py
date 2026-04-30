from message import Message
from event import Event, EventType
from scheduler import Scheduler
# from queue import Queue
# from client import Client
# from server import Server
# from gateway import Gateway


class Engine:
    def __init__(self):
        self.trace_id = 1  # not used in table, but can be useful later

    #  TRACE HEADER 
    def print_trace_header(self):
        print(f"{'time':<8} {'node':<5} {'event':<6} {'source':<7} {'dest':<7} {'msgID':<5}")
        print("-" * 50)

    # GENERATE TRACE (TABLE FORMAT)
    def generate_trace(self, event):
        message = event.get_message()

        time = event.get_event_time()
        event_type = event.get_event_type().value
        source = message.get_source()
        destination = message.get_destination()
        msg_id = message.get_message_id()

        # Temporary node (will improve later)
        node = source

        print(f"{time:<8.3f} {node:<5} {event_type:<6} {source:<7} {destination:<7} {msg_id:<5}")

    # TEST MESSAGE
    def test_message(self):
        print(" Testing Message ")
        msg1 = Message("Client", "Gateway")
        msg2 = Message("Client", "Server")

        msg1.print_message()
        msg2.print_message()
        print()

    # TEST EVENT 
    def test_event(self):
        print(" Testing Event ")
        msg = Message("Client", "Gateway")
        event = Event(0.5, EventType.SEND_MSG, msg)

        event.print_event()
        print()

    #  TEST SCHEDULER
    def test_scheduler(self):
        print(" Testing Scheduler ")
        scheduler = Scheduler()

        msg1 = Message("A", "B")
        msg2 = Message("A", "B")
        msg3 = Message("A", "B")

        e1 = Event(2.0, EventType.SEND_MSG, msg1)
        e2 = Event(1.0, EventType.RECV_MSG, msg2)
        e3 = Event(3.0, EventType.MSG_DEPT, msg3)

        scheduler.add_event(e1)
        scheduler.add_event(e2)
        scheduler.add_event(e3)

        scheduler.print_events()
        print()

    # TEST TRACE
    def test_trace(self):
        print("=== Testing Trace Table ===")

        self.print_trace_header()

        msg1 = Message("1", "0")
        msg2 = Message("3", "0")

        e1 = Event(1.202, EventType.SEND_MSG, msg1)
        e2 = Event(1.916, EventType.RECV_MSG, msg1)
        e3 = Event(2.320, EventType.SEND_MSG, msg2)

        self.generate_trace(e1)
        self.generate_trace(e2)
        self.generate_trace(e3)

        print()
    # # TEST QUEUE
    # def test_queue(self):
    #     print("=== Testing Queue ===")
    #     q = Queue()
    #     msg1 = Message("Client1", "Gateway")
    #     msg2 = Message("Client2", "Gateway")
        
    #     q.enqueue(msg1)
    #     q.enqueue(msg2)
    #     q.print_queue()
        
    #     removed_msg = q.dequeue()
    #     print(f"\nDequeued Message ID: {removed_msg.get_message_id()}")
    #     q.print_queue()
    #     print()

    # # TEST CLIENT
    # def test_client(self):
    #     print("=== Testing Client ===")
    #     # lambda = 4 per second
    #     client = Client(1, 4)
    #     client.print_client()
        
    #     msg = client.create_message("Gateway")
    #     print("Created:", end=" ")
    #     msg.print_message()
        
    #     print(f"Next arrival in: {client.get_next_arrival_time():.4f} seconds\n")

    # #  TEST SERVER 
    # def test_server(self):
    #     print("=== Testing Server ===")
    #     # mu = 8 per second
    #     server = Server(1, 8)
    #     server.print_server()
        
    #     print(f"Service time for a message: {server.get_service_time():.4f} seconds\n")




    #  #  MAIN SIMULATION LOOP
    # def run_simulation(self, sim_time, lambda_rate, mu_rate):
    #     print(f"\n=== Starting Simulation (Time: {sim_time}s, Lambda: {lambda_rate}, Mu: {mu_rate}) ===")
        
    #     # 1. Initialize the system components
    #     scheduler = Scheduler()
    #     client = Client(1, lambda_rate) # Client ID 1
    #     queue = Queue()
    #     server = Server(0, mu_rate)     # Server ID 0 (based on slide 16 trace)
    #     gateway = Gateway(queue, server)

    #     # 2. Schedule the very first SEND_MSG event to kickstart the loop
    #     first_arrival_time = client.get_next_arrival_time()
    #     first_msg = client.create_message(server.get_server_id())
    #     first_event = Event(first_arrival_time, EventType.SEND_MSG, first_msg)
    #     scheduler.add_event(first_event)

    #     self.print_trace_header()

    #     # 3. The Main Loop
    #     while not scheduler.is_empty():
    #         # Get the next event
    #         current_event = scheduler.get_event()
    #         current_time = current_event.get_event_time()

    #         # Stop if we exceed the simulation time
    #         if current_time > sim_time:
    #             break

    #         # Print the event to our trace table
    #         self.generate_trace(current_event)

    #         # --- Handle SEND_MSG ---
    #         if current_event.get_event_type() == EventType.SEND_MSG:
    #             # a. Schedule the arrival at the gateway (1 second delay per Slide 10)
    #             recv_time = current_time + 1.0
    #             recv_event = Event(recv_time, EventType.RECV_MSG, current_event.get_message())
    #             scheduler.add_event(recv_event)

    #             # b. Schedule the next message generation for the client
    #             next_arrival = current_time + client.get_next_arrival_time()
    #             next_msg = client.create_message(server.get_server_id())
    #             next_send_event = Event(next_arrival, EventType.SEND_MSG, next_msg)
    #             scheduler.add_event(next_send_event)

    #         # --- Handle RECV_MSG ---
    #         elif current_event.get_event_type() == EventType.RECV_MSG:
    #             # Gateway decides if it goes to server or queue
    #             dept_event = gateway.receive_message(current_event.get_message(), current_time)
    #             # If it went to the server, schedule the departure
    #             if dept_event is not None:
    #                 scheduler.add_event(dept_event)

    #         # --- Handle MSG_DEPT ---
    #         elif current_event.get_event_type() == EventType.MSG_DEPT:
    #             # Gateway frees the server and pulls from queue if needed
    #             next_dept_event = gateway.process_departure(current_time)
    #             # If a message was pulled from the queue, schedule its departure
    #             if next_dept_event is not None:
    #                 scheduler.add_event(next_dept_event)

    # -------- RUN ALL TESTS --------
    def run_tests(self):
        self.test_message()
        self.test_event()
        self.test_scheduler()
        self.test_trace()

        # # Session 2 Tests
        # self.test_queue()
        # self.test_client()
        # self.test_server()


# -------- MAIN --------
if __name__ == "__main__":
    engine = Engine()

    engine.run_tests() 
    
    # # Run a short 10-second simulation with lambda=4 and mu=8
    # engine.run_simulation(sim_time=10, lambda_rate=4, mu_rate=8)