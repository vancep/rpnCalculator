#!/usr/bin/env python

# create a JSON-RPC-server
import jsonrpc
server = jsonrpc.Server(jsonrpc.JsonRpc20(), jsonrpc.TransportTcpIp(addr=("127.0.0.1", 31415), logfunc=jsonrpc.log_file("myrpc.log")))

# define some example-procedures and register them (so they can be called via RPC)
def echo(s):
    return s

server.register_function( echo )

# start server
server.serve()
