Lecture 1/30
Functions are first class: functions are values 
	in python
higher-order function: EITHER takes a function as an 
	argument valyue OR returns a function as a return value

def apply_twice(f,x):
	return(f(f(x)))

def square(x):
	return x*x
f applies to function we are doing twice 
do inside then outside?!?!? ()

def make_adder(n):
	def adder(k):
		return n+k
	return adder
add_three = make_adder(3)
	add_three is bound to the VALUE of make_adder(3)
	 [which is another function!]

parent of a function = frame where it is created/defined
nested def: def statement inside another def statement
if a def is indented: parent frame = local frame
the parent of a frame is the parent of the function called
*copy the parent of the function to the local frame

Local Names
def f(x,y):
	return g(x)
def g(a):
	return a+y
f(1,2) = g(1) = 
WRONG: it breaks bc when g(a) frame calls on y it looks
 in the global frame but there isnt a y, y is not in the
 environment


 def compose1(f,g):
 	def h(x):
 		return f(g(x))
 	return h
 def 

 lambda expression
square = lambda x: x*x
instead of square = x*x
can create a function without giving it a Name
a function with formal parameter x that returns the valeu
of x*x
no return statement
restricted to short functions
only one return expression in body
lambda x,y

 QQQ: do we execute (create frame for) operator or operands first?









