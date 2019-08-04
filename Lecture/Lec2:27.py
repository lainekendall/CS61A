Lec2/27.py
object oriented programing
inheritance!!
	way of relating similar classes together
	common use: specializedclass inherits from a more general class 
	class <new class>(<base class>)
	new classs shares attributes with the base class, and overrieddes certain attributes
	implementing new class is now as simple as specifying how it's different from base class 
	EX: class Account:
		BANK accounts have: [attributes!!] accoutn holder, balance, interest rate
		you can: deposit to an account, withdraw [methods!!]
		class CheckingAccount(Account):
				attributes: account holder, balance, interst rate of 1%, withdraw fee of $1
				methods: deposit, withdraw (w/ fee)
	attribute look up
	if the name is n the attributes of the class, return corresponding value
	if not look in base class, if there is orientedbase class attributes are NOT copied into sublclasses

Design for inheritance
	don't repeat yourself!! use existing implementations
	reuse overridden attributes by accessing them through bae class 
	look up attributes on instances if possible
	always use self.whatever unless the variable is defined globally

inheritance vs. composition
	inheritance: relating two classes through specifiyign similarities and difs
	represents "is a" relationshps, ex checking account is type of account
	composition: connecting two classes through their relationship to one another
	represents "has a" relationships, ex bank has a collection fo accounts

Multiple inheritance
	class can inherit from multiple base classes
	if using multiple classes, python reads left to right, left class will be looked in first

complicated inheritance
	don't overuse it!
	biological inheritance
	