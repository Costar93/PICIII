import zmq
import random



# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

# Run a simple "Echo" server
while True:
    message = sock.recv()
    if message is not None:
        aleatori = random.randint(0, 20)
    sock.send("Echo: "  + str(aleatori))
    print "Echo: " + str(aleatori)
