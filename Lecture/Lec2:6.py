Lec2/6.py
1 pimentel but check!!
no lab on Tues!!!
hog strategy contest concludes 2/18 11:59pm



Abstraction: giving a name to something
	Fuctional Abstraction
		What does sum_squares need to know about square?
		needs to know that square takes one argument
		need to know its name
		do you need to know square's intrinsic name?? (the name it was named in the def statement)
			NO does not need to know intrinsic name
		does it need to know that square computes x*x? Yes
		does it need to know how square computes it, by calling mul? no
			could be pow(x,2) or mul(x,x)...doesn't matter

	Choosing Names
		matters a lot for composition
		names should convey the meaning or puspose of the values to which they are bound
		type of value bound to the name is best documented in a function's DOCSTRING
		use all lowercase!
	Which Values Deserve a Names
		repeated compound expressions
		if you refer to something two or more times, give a new name!!

		meaningful parts of complex expressions:
		don't write everything in one line of code, split it up

		tips:
		names can be long if they help document your code
		names can be short for simple examples, 
			n, i, k: usually integers
			x, y, z: real
			f, g, h: functions

		develop your own style, don't have to follow these rules

Testing
	Test-Driven Development
	write the test of a function before you write the function
	tests clarify the domain, range, and behavior of a function
	tests can help identify tricky edge cases
	develop incrementally and test each piece before moving on
	run old tests again after you make new changes
	run code interactively
	experiment with a function after you write it

@trace
def gcd(m,n):
	"""return the largest k that evenly divides both m and n
	k,m and n are all positive integers.
	>>>gcd(12,8)
	4
	>>>gcd(16,12)
	4
	>>>gcd(2,16)
	2
	>>>gcd(24,42)
	6
	>>>gcd(5,5)
	5
	"""
	if m == n: change to if m % n == 0: then return n (and vice versa)
		return m
	elif m < n:
		return gcd(n,m)
	else:
		return gcd(m-n, n)

Euclidian algorithm
trace examples so that you can see what is more efficient

Decorators
	Function Decorators: @trace
		replaces your function with trace
		higher order function that returns a functio
	if you put @function above def of a function, same as defining the function and then
	binding its name to the function of a Decorators

	@trace
	def gcd

	is the same as
	def trace
	def gcd
	trace(gcd)

Currying == add to make_adder
	Function Currying
	higher order producure that transforms a higher order function into a function

def make_adder(n):
	return lambda k: n + k

>>>make_adder(2)(3)
5
curried version of add can store first value for variable

Review
What would python print?
print function returns none. it also displays its arguments (separated by spaces) when it's called
print(5) evalues to none, interactive output = 5
print(print(5)) evaluates to None, prints 5 AND None
order that things get evaluated(evaluate the operator and operand expressions before you call the functions)

within a frame you can have one name bound to only one thingsreplace old assignment with new assignment












