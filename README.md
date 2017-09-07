# rpnCalculator
A JSON RPC back-end for a multi-session RPN calculator  

## Some resources
http://www.jsonrpc.org/  
http://www.jsonrpc.org/specification  
http://www.simple-is-better.org/rpc/  

**Method**  
open  
**Parameter**  
N/A (N/A)  
**Result**  
session_id (integer)  
**Method Description**  
Open a new session. Return the session ID.  

**Method**  
push  
**Parameter**  
session_id (integer)   
**Result**  
stack array  
**Method Description**  
Push a number to the stack in the specified session.  

**Method**  
pop  
**Parameter**  
session_id (integer)  
**Result**  
number stack (integer array	)
**Method Description**  
Pop a number from the stack in the specified session.  

**Method**  
clear  
**Parameter**  
session_id (integer)  
**Result**  
N/A (N/A)  
**Method Description**  
Clear the stack of the specified session. Return null.  

**Method**  
add  
**Parameter**  
session_id 	integer  
**Result**  
stack (array)  
**Method Description**  
Pop two numbers from the stack, add them, and put the result back onto the stack.   

**Method**  
subtract  
**Parameter**  
session_id (integer)  
**Result**  
stack (array)  
**Method Description**  
Pop two numbers from the stack, subtract them, and put the result back onto the stack.   

**Method**  
close  
**Parameter**  
session_id (integer)  
**Result**  
N/A (N/A)  
**Method Description**  
Close the specified session. Return null.  

## Errors

**Code	Message**  
1		Invalid session ID  
2		Insufficient number of stack items  
