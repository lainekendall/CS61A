## Extra Object-Oriented Programming questions ##

from lab06 import *

# Q7
class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> check = Check("Steven", 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # trying to steal steven's money
    The police have been notified.
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # can't cash check twice
    The police have been notified.
    """
    withdraw_fee = 1
    interest = 0.01

    def __init__(self, account_holder):
        Account.__init__(self, account_holder)

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    def deposit_check(self, check):
        if check.name == self.holder and check.amount:
            money = check.amount
            check.amount = 0
            return Account.deposit(self, money)
        else:
            print("The police have been notified.")

class Check(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    @property 
    def deposited(self):
        return self.amount == 0

# Q8
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.pressed
    2
    >>> b2.pressed
    3
    """

    def __init__(self, *args):
        self.buttons = args

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        button = self.buttons[info]
        button.pos = info
        button.pressed += 1
        return button.key

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        lst = []
        for x in typing_input:
            lst += [self.buttons[x].key]
            self.buttons[x].pressed += 1
        return ''.join(lst)

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0
