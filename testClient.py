#!/usr/bin/env python

# create JSON-RPC client
import jsonrpc
server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(), jsonrpc.TransportTcpIp(addr=("127.0.0.1", 31415)))

# call a remote-procedure (with positional parameters)

#result = server.echo("hello world", True, 42)

#result2 = server.echo("hi")

result = server.open(True, 43)
id = result["session_id"]

server.push(id, 5, True, 44)

server.push(id, 6, False)

server.push(id, 2)

server.add(id, True, 45)

server.push(id, 2, True, 46)

server.subtract(id, True, 47)

server.pop(id, True, 48)

server.getStack(id, True, 49)

server.close(id)
