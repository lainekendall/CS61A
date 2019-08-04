lec2/18.py
homework 4 due monday
project is really hard and big
bonus point early submission
project party on tuesday

Box-and-pointer notation
	the closure property of data types
	method for combining data values satisfies the closure property if:
		result of combo can itself be combined using the same method
	closure is powerful bc we can create structures
	heirarcchical structures are made up of parts, which themselves are made up of parts
	lists are index-lableled adjacent boxes,
	contains arrow or values
Sequence operations
	membership & slicing
		Membership: in, not in 
			2 in [1,2,3]
		Slicing: digits[0:2] does not include index# 2
			always creates a new list

Trees
	Tree Abstraction
		Tree has root value and sequence of branches, each branch is a Tree
		tree with zero branches is a leaf
		node: sub root
		tree is a constructor
		if you put branches=[] into argument it asserts that it must be a list

Tree Processing
	uses recursion
	processing a leaf is often the base case of a tree processing functin
	recursive call on each branch
sum([leaves(b) for b in branches(tree), []])

Partition Trees (sum up numbers at most m to get n)
	


