#!/usr/bin/env python

# create a JSON-RPC-server
import jsonrpc
server = jsonrpc.Server(jsonrpc.JsonRpc20(), jsonrpc.TransportTcpIp(addr=("127.0.0.1", 31415), logfunc=jsonrpc.log_file("myrpc.log")))

# define some example-procedures and register them (so they can be called via RPC)
def echo(s):
    return s

# Open a new session. Return the session ID.
def open():
    return -1

# Push a number to the stack in the specified session.
def push(id):
    return -1

# Pop a number from the stack in the specified session
def pop(id):
    return -1

# Clear the stack of the specified session. Return null.
def clear(id):
    return None

# Pop two numbers from the stack, add them, and put the result back onto the stack.
def add(id):
    return -1

# Pop two numbers from the stack, subtract them, and put the result back onto the stack.
def subtract(id):
    return -1

# Close the specified session. Return null.
def close(id):
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
