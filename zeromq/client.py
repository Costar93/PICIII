import zmq
import sys
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")
while True:
    # Send a "message" using the socket
    #sock.send(" ".join(sys.argv[1:]))
    sock.send("Hola amigo")
    print sock.recv()
    time.sleep(5)
