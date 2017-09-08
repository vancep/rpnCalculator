#!/usr/bin/env python

# Create a JSON-RPC-server
import jsonrpc, threading

# Custom JSON-RPC 2.0 error-codes
INVALID_SESSION_ID_ERROR = 1
INSUFFICIENT_NUM_STACK_ITEMS = 2
OUT_OF_SESSION_IDS = 3

server = jsonrpc.Server(jsonrpc.JsonRpc20(), jsonrpc.TransportTcpIp(addr=("127.0.0.1", 31415), logfunc=jsonrpc.log_file("myrpc.log")))
lock = threading.Lock()
idIndex = 0
sessions = {}

class OpenSessionError(jsonrpc.RPCFault):
    def __init__(self, error_data=None):
        jsonrpc.RPCFault.__init__(self, OUT_OF_SESSION_IDS, "Out of session IDs. Reached max integer.", error_data)

class InvalidSessionIdError(jsonrpc.RPCFault):
    def __init__(self, error_data=None):
        jsonrpc.RPCFault.__init__(self, INVALID_SESSION_ID_ERROR, "Invalid session ID.", error_data)

class InsufficientNumStackItemsError(jsonrpc.RPCFault):
    def __init__(self, error_data=None):
        jsonrpc.RPCFault.__init__(self, INSUFFICIENT_NUM_STACK_ITEMS, "Insufficient number of stack items.", error_data)

# Checks if ID is in use. Returns True if ID in use.
def idInUse(sid):
    if sid in sessions.keys():
        return True

    return False

# define some example-procedures and register them (so they can be called via RPC)
def echo(s):
    return s

# Open a new session. Return the session ID.
def open():
    global idIndex
    lock.acquire()

    try:
        while(idInUse(idIndex)):
            idIndex += 1

        sessions[idIndex] = [] # creates a empty stack for new session

        lock.release()

        return idIndex

    except OverflowError as e:
        lock.release()
        raise OpenSessionError(error_data)
        sys.exit(1)

open()
# Push a number to the stack in the specified session.
def push(sid, value):
    if(idInUse(sid)):
        pass
    else:
        raise InvalidSessionIdError(sid + " is not a valid session ID.")
    return -1

# Pop a number from the stack in the specified session
def pop(sid):
    return -1

# Clear the stack of the specified session. Return null.
def clear(sid):
    return None

# Pop two numbers from the stack, add them, and put the result back onto the stack.
def add(sid):
    return -1

# Pop two numbers from the stack, subtract them, and put the result back onto the stack.
def subtract(sid):
    return -1

# Close the specified session. Return null.
def close(sid):
    return None

server.register_function( echo )
server.register_function( open )
server.register_function( push )
server.register_function( pop )
server.register_function( clear )
server.register_function( add )
server.register_function( subtract )
server.register_function( close )

# start server
server.serve()
