Lec2/4.py

announcements
	review sessions 2/8 1 pimentel 1-2:30 and 2:30-4
	hkn review session on saturday 2/7 (2050 vlsb 1-4)
	friday is review lecture
	one page both sides of hand written-notes
	look up study guide (provided on back of exam)

Order of Recursive Calls
	cascade function

def cascade(n):
	if n < 10:
		print (n)
	else:
		print (n)
		cascade(n//10)
		print(n)

cascade is in between print statements: why?
	bc you don't finish each cascade function until you finish the next cascade function'
	order = first print of 123, first print of 12, print of 1, second print of 12, second print of 123

Two definitions of cascade
	can remove the base case! in this just put in print before
which is better? 
should keep the base case, and should put it first

example: inverse cascade

def inverse_cascade(x):


grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

Tree Recursion
	tree-shaped processes arise whenever executing the body of a recursive function makes more than one recursive call
	MORE than 1!
	root is the intitial thing you are calculating (fib(5))

Project
	trace: prints out if a function is called or returned
	check for # prints and returns
	number of recursive calls = number of branches

ex. counting partitions
count_partictions(n,4)
	two possibilities:
		uses at least one 4: partition is of n-4 and 4
			count partitions of n-4
		does not use any 4
			count_partictions(n-1)

	do this same process over and over again








