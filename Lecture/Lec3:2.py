Lec3/2.py
String representations
	an object value should behave like the kind of date it's meant to represent
	producing a spring representation of itself
	all objects have two reps:
		str = humans
		repr = python
	repr String
	gives a python exp
	eval(repr(object)) = object

Polymorphic functions
	function that applies to many different forms of data
	both str and repr
	repr invokes zero argument method __repr__ on its argument

	an instance attrivute called __repr__ is ignored by repr function, only class attributes are found
	if no __str__ attribute is found, it gives back repr

def repr(o):
	return type(o).__repr__(o)

def str(o):
	return 

Interface
	message passing: objects interact by looking up attributes on each other (passing messages)
	attribute look-up rules allow dif data types to respond to same message
	shared message (attribute name) that elicits similar behavior from dif objects is abstraction!
	interface is set of shared messages, along with specification of what they mean 

Property Methods
	special kind of method, looks like reg attr 
	attributes that update automatically
	@Property
		lets you call things without parenthesis

Complex Numbers
	represented on graphs: both rectangular and polar
	assume there are two dif kinds
	1 + sqrt(-1) 	= 	complexRI(1,1) 	= 	complexMA(sqrt(2), pi/4)

class Complex:
	def add(self, other):

should have: real and complex components, magnitude and angle
so we need to define a class of complex and two subclasses!!






