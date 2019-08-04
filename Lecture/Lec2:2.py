Lec2/2
programs should be concise, well-named, understandalbe, and easy to follow
	composition feedback, 2 points
	comment your code ###
	define own functions to break up
midterm 1: up thru wednesday 2/4
friday = review
monday = no lecture

recursive functions:
	def the body of the function calls itself, either directly or indirectly
	implication: executing the body of a recursive function may requre applying that function

digit sums:
	2+0+1+5 = 8
sum digits without a while statment!
	
def split(n):
	"""split positive n into all but its last digit and its last digit."""
	return n // 10, n % 10
def sum_digits(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last
anatomy of recursive
	def statment header
	conditional cases check for base case / simple instance (where you don't need a function)
	recursive case: 

environment diagrams
def sstatment: new function /frame
	your if statent must have a return value in addition to the other part
only will work if the recursive part of the problem is simpler than the rest!!
	n has to go down to 0 or else it won't stop looping

iteration vs. recursion
	iteration is a special case of recursion (while loops)

def fact(n):
	total, k = 1, 1
	while k <= n:
		total, k = total*k, k +1
	return total

verifying recursive functions
	1. verify the vase case
	2. treat fact as a functional abstraction!
		don't worry about how fact function works, just think about what it does
	3. assume that fact(n-1) is correct
	4. verify that fact(n) is correct

verify digit sum
	1. base case: 

mutual recursion
	lund algorithm: used to verify credit cards

def lund_sum(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return lund_sum_double(all_but_last) + last

def luhn_sum_double(n):
	all_but_last, last = split(n)
	luhn_sum_double



