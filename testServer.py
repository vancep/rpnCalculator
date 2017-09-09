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
def echo(s, isReq=False, id=0):
    return s

# Open a new session. Return the session ID.
def open(isReq=False, id=0):
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

# Push a number to the stack in the specified session.
def push(sid, value, isReq=False, id=0):
    if(idInUse(sid)):
        sessions[sid].append(value)
        return sessions[sid]
    else:
        raise InvalidSessionIdError(str(sid) + " is not a valid session ID.")
        sys.exit(1)

# Pop a number from the stack in the specified session
def pop(sid, isReq=False, id=0):
    if(idInUse(sid)):
        if(len(sessions[sid]) > 0):
            value = sessions[sid].pop()
            return value
        else:
            raise InsufficientNumStackItemsError("Insufficient number of stack items.")
    else:
        raise InvalidSessionIdError(str(sid) + " is not a valid session ID.")

    sys.exit(1) # is only reached if not able to sucessfully perform operation

# Clear the stack of the specified session. Return null.
def clear(sid, isReq=False, id=0):
    if(idInUse(sid)):
        sessions[sid] = {}
        return none
    else:
        raise InvalidSessionIdError(str(sid) + " is not a valid session ID.")
        sys.exit(1)

# Pop two numbers from the stack, add them, and put the result back onto the stack.
def add(sid, isReq=False, id=0):
    if(idInUse(sid)):
        if(len(sessions[sid]) > 1):
            op1 = sessions[sid].pop()
            op2 = sessions[sid].pop()

            sessions[sid].append(op1 + op2)

            return sessions[sid]
        else:
            raise InsufficientNumStackItemsError("Insufficient number of stack items.")
    else:
        raise InvalidSessionIdError(str(sid) + " is not a valid session ID.")

    sys.exit(1) # is only reached if not able to sucessfully perform operation

# Pop two numbers from the stack, subtract them, and put the result back onto the stack.
def subtract(sid, isReq=False, id=0):
    if(idInUse(sid)):
        if(len(sessions[sid]) > 1):
            op1 = sessions[sid].pop()
            op2 = sessions[sid].pop()

            sessions[sid].append(op1 - op2)

            return sessions[sid]
        else:
            raise InsufficientNumStackItemsError("Insufficient number of stack items.")
    else:
        raise InvalidSessionIdError(str(sid) + " is not a valid session ID.")

    sys.exit(1) # is only reached if not able to sucessfully perform operation

def getStack(sid, isReq=False, id=0):
    if(idInUse(sid)):
        return sessions[sid]
    else:
        raise InvalidSessionIdError(str(sid) + " is not a valid session ID.")

    sys.exit(1) # is only reached if not able to sucessfully perform operation

# Close the specified session. Return null.
def close(sid, isReq=False, id=0):
    if(idInUse(sid)):
        del sessions[sid]
        return none
    else:
        raise InvalidSessionIdError(str(sid) + " is not a valid session ID.")
        sys.exit(1)

server.register_function( echo, "null" )
server.register_function( open, "session_id" )
server.register_function( push, "stack" )
server.register_function( pop, "number" )
server.register_function( clear, "null")
server.register_function( add, "stack" )
server.register_function( subtract, "stack" )
server.register_function( getStack, "stack" )
server.register_function( close, "null" )

# start server
server.serve()
