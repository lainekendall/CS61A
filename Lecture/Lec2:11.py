Lec2/11.py
announcements
	guerrilla section saturday 2/14 on recursion
	hw 3 posted today due next wednesday
	hw party in 2050 vlsb at 5pm

Data Abstraction: chapter 2
	compound values combine other values together
	a date: year, month, day [combines all into one thing]
	geographic: latitude and longitutde
	data abstraction allows us to manipulate compound values as units (giving something a name, treating it as a whole)
	isolate two parts of any program
		how data are represented (as parts)
		how data are manipulated (as units)
	a way in which functions enforce an abstraction barrier between representation and use

Rational Numbers
	exact representation of fractions (1/3 vs. .333333.....)
	a = n/d
	as soon as divide occurs, the exact representation may be lost
	python truncates decimal representations (unlike integers)
	floating point number is inexact (unlike integer)
	type(3) == int
		function: rational(n,d) returns a rational number x [constructor]
		numer(x) returns the numerator of x, n [selector]
		denom(x) returns denominator of x [selector]

Pairs
	Representing pairs using lists
	pair = [1,2]
	>>>pair
	[1,2]
	x,y = pair
	(so then x =1 and y =2)     UNPACKINg
	pair[0]                  ELEMENT SELECTION
	1 (bc 1 is the 0th element of the list)
	getitem(pair,0) = 1 

Reducing to Lowest Terms
	from fractions import gcd

Abstraction Barriers
	Parts of the Program that....   Treat rationals as...      using
	use rational numbers to 
	if you are using whole data values you should never call rational, numer, or denom

BAD things to doL
	add_rational([1,2],[1,4])	     MUST use constructions
	def divide_rational(x,y):
		return [x[0]*y[0], x[1], y[1]]   MUST use selectors, and then constructors

Data representations
	Behavior Condition:if we construct x from n and d, then numer(x)/denom(x) must equal n/d
	if behavior conditions are met, representation is valid
	you can recognize an abstract data representation by its behavior
	can use functions instead of lists










