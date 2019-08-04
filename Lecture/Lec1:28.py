Lecture 1/28
Fibonancci Sequence
	0th element: 0
	0 1 1 2 3 5 8...
	creates a spiral in squares with side lengths of the #s
Generalization
	generalizing patterns with arguments
	   regular geometic shapes relate length and area
	   Area(square)=r^2
	   Area(circle)=pi r^2
assert 3>2, 'Math is broken'
	nothing will happen
assert 3<2, 'That is false'
	if it's false, then you get an error message displaying That is false
assert statements stop execution! if before return statements or etc.
Higher order Functions

def sum_naturals(n):
	total, k = 0 , 1
	while k<=n:
		total, k = total + k, k+1
	return total
def sum_cubes(n):
	total , k = 0, 1
	while k<= n
		total, k = total + pow(k,3), k+1
	return total
def identity(k):
	return k
def cub(k):
	return pow (k,3)

def summation:
	total , k = 0 , 1
	while k<=


Functions as return values
	two types of functions: 
		locally defined functions
		functions defined within other functions bodies
		 are bound to naems in a local frame
def make_adder(n):
	def adder(k):
		return n+k
	return adder


	compound operator: make_adder(3)






