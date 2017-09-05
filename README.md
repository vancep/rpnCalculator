# rpnCalculator
A JSON RPC back-end for a multi-session RPN calculator  

**Method		Parameter			Result							Method Description**  
**			Name		Type	Name			Type**  
open		N/A			N/A		session_id		integer			Open a new session. Return the session ID.  
push 		session_id	integer stack 			array 			Push a number to the stack in the specified session.  
pop 		session_id 	integer number stack	integer array	Pop a number from the stack in the specified session.  
clear 		session_id 	integer N/A 			N/A 			Clear the stack of the specified session. Return null.  
add 		session_id 	integer stack 			array 			Pop two numbers from the stack, add them, and put the result back onto the stack.   
subtract	session_id 	integer stack 			array 			Pop two numbers from the stack, subtract them, and put the result back onto the stack.   
close 		session_id 	integer N/A 			N/A 			Close the specified session. Return null.  
  
##Errors

**Code	Message**  
1		Invalid session ID  
2		Insufficient number of stack items  
