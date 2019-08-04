Lec2/13.py
homework party tuesday 
Sequences
	Sequence Abstraction
	there isn't one sequence class or data Abstraction
	sequence abstraction is a collection of behaviors:
		Length: sequence has a finite Length
		element selection: sequence has an element corresponding to any non-negative integer index less than its length starting at 0
		list is a kind of sequence

list
	lists are Sequences
	can add lists
	can multiply lists (2*[1,2] = [1,2,1,2])
	list within a list: [[10,20],[30,40]] = pairs
	pairs[0] = [10,20]
	pairs[0][1] = 30

for loops
	can be stopped with a return statement

Sequence Iteration
	for x in s:			x is bound in first frame in current enviro(does not create a new enviro)
	1. Evaluate the header expression, which must yield an iterable value (a sequence)
	2. for each element in that sequence:
		a. bind name to element
		b. execute the suite
Unpacking sequences in for statements
pairs = [[1,2],[2,2],[3,2]
for x,y in pairs

Ranges
	sequence of consecutive integers
	range(-2,2)		from before the -2 until before 2
	includes -2,-1,0,1
	length= ending value - starting value
	list(range(-2,2)) = -2,-1,0,1
	range(4) = range(0,4)
	range(4)[2] = 2
	for _ in range(3):	not using the _ bc it doens't appear anywhere in the code
	square brackets can be used for all types of sequences

List Comprehensions
	
def divisors(n):
	return [1] +[x for x in range(2,n) if n%x==0]
	[map expression for name in iter expression if filter expression
	a combined expression taht evaluates to alist using:
	1. add a new frame within the current frame as its parent
	2. Create an empty result list that is the value of the expression
	3. for each element in iterable value of iter expression
	4. bind name to that element in the new frame

Strings: sequences of letters (characters)	
	how to execute strings: exec('string')
	\n means going to new line
	\a escapes following character(a in this case)
	an element of a string is also a string

Dictionaries
	{'I': 1, 'V':5, 'X': 10}
	no control over order of elements
	





