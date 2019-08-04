Lec2:23.py
extra office hours 11-6 wednesday
Mutable Material
	function with behaviour that varies over time
	bank account:
		withdraw(25) and returns remaining balance
	remember: function has a body and a parent environment
nonlocal assignment:
	nonlocal balance: changes the balance in the parent frame
	nonlocal vs global: 

Non-local assignment:
	nonlocal <name>
	effect: future assignments to that name change its pre-existing binding in the first 
	non-local frame of the current environemtn in which name is bound
if x = 2
status
no non-local statement
nonlocal doesn't bind to something in the global frame '

Python particulars
	python pre-computes which frame contains each name before executing body of a function
	within body of a function, all instances must refer to same frame
Mutable values
	you could use mutable lists instead of nonlocal values

Multiple Mutable Functions
	can keep track of things

Lost Referential Transparency
	x = 4
	return g
	g(2)
	y = 2
	H(3)
5 + 3 + 