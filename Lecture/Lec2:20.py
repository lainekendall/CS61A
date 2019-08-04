Lec2:20.py
project party tuesday
bonus point wednesday

Objects
	date: built in function, a class
	objects represent information
	they consist of data and behavior, bundled together to create abstractions
	objects can repersent things, properties, interactions
	classes are first-class
	object oriented programming
	metaphor for organizing large programs
	special syntax that can improve composition of programs(.)
		in python every value is an object
		all objects have attributes
		data manipulation happens through object methods
		functions do one thing, objects do many related behaviors

	Strings: an object

Mutation
	some objects can change
	list.pop(): removes last element and returns it
	list.remove('start'): removes start from list
	list.append: adds one element to end
	list.extend: adds multiple elements
	the list will change no matter what, no way to acces original list
	all names that refer to same object are affected by Mutation

Dictionaries are unordered collections of key-valued pairs
	restrictions:
		key cannot be a list or any mutable type
		two keys cannot be equal
		first restriction is tied to pythons underlying implementation of Dictionariessecond restriction is part of the dictionary abstraction
		{'odds': [1,3,4,7]}

Mutation
	can happen within a function call
	a function can change the vale of any object in its scope

Tuples
	immutable sequence!!
	(3,4) or 3,4
	(): empty tuple
	tuple([1,2])
	can be used as item in dictionary
	**value of an expression can change bc of changes in names or objects
	object mutation: not changing name but actually changing object
	if a list is inside a tuple then you can change the list inside but not anything else

sameness and change
	as long as we never modify objects, a compound object is just the toatality of its pieces

identity operators
	is: a is b will be true ONLY if they refer to the same object
	==: equality is true only if the values are the same



