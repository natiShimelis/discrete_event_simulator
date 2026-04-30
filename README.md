# Discrete Event Simulator

A discrete event simulator built in Python for the **Performance Evaluation of Connected Systems** course (NCA — USEEJ7) at CNAM.

## Overview

This simulator models a probabilistic system where a client sends messages through an IoT gateway (queue + server). It tracks system variables over time and computes performance metrics such as average waiting time and number of requests in the system.

## Architecture

The simulator follows an object-oriented design where each component is its own class:

| File | Class | Description |
|------|-------|-------------|
| `engine.py` | Engine | Main entry point, stores simulation parameters and runs the simulation |
| `scheduler.py` | Scheduler | Maintains a chronologically ordered list of events |
| `client.py` | Client | Generates messages with exponentially distributed inter-arrival times |
| `gateway.py` | Gateway | IoT gateway that receives and processes messages |
| `server.py` | Server | Processes messages with exponentially distributed service times |
| `queue.py` | Queue | Holds messages waiting to be served |
| `event.py` | Event | Represents a simulation event (SEND_MSG, RECV_MSG, MSG_DEPT) |
| `message.py` | Message | Represents a message with timestamp, source, and destination |

## Event Types

- **SEND_MSG** — Client sends a message to the gateway (1 second propagation delay)
- **RECV_MSG** — Gateway receives the message
- **MSG_DEPT** — Gateway completes processing a message (service departure)

## Parameters

- `lambda (λ)` — Message inter-arrival rate (tested at 4, 6, 8, 12 per second)
- `mu (μ)` — Gateway service rate (8 per second)
- `nClients` — Number of clients
- `nServers` — Number of servers in the gateway
- `simTime` — Total simulation time

## Metrics Collected

- Instantaneous number of requests in the system and queue
- Total number of requests processed
- Average number of requests in the system and queue
- Average waiting time in the system and queue
- Number of dropped messages (for finite queue simulations)

## Simulations

| Scenario | Servers | Queue Capacity | Notes |
|----------|---------|----------------|-------|
| M/M/1 | 1 | Unlimited | Base case |
| M/M/1/4 | 1 | 4 | Tracks dropped messages |
| M/M/1/8 | 1 | 8 | Tracks dropped messages |
| M/M/3/8 | 3 | 8 | Multi-server |

All simulations are run with λ = 4, 6, 8, 12 and results are plotted with 95% confidence intervals.

## Trace Output

After each event, the simulator generates a trace in the following format:

```
time    node    event   source  dest.   msgID
1.202   1       SEND    1       0       1
1.916   0       RECV    1       0       1
4.572   0       DEPT    1       0       1
```

## How to Run

```bash
python engine.py
```

## Course Info

- **Course:** Performance Evaluation of Connected Systems (USEEJ7)
- **Institution:** CNAM
- **Lab:** Lab 2 — Discrete Event Simulator