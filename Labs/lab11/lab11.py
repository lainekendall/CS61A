#############
# Iterators #
#############
class IteratorA:
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 100:
            raise StopIteration
        self.start += 5
        return self.start

    def __iter__(self):
        return self

class IteratorB:
    def __init__(self):
        self.start = 5

    def __iter__(self):
        return self

class IteratorC:
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 10:
            raise StopIteration
        self.start += 1
        return self.start

class IteratorD:
    def __init__(self):
        self.start = 1

    def __next__(self):
        self.start += 1
        return self.start

    def __iter__(self):
        return self

class IteratorRestart:
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.curr == self.end:
            raise StopIteration
        self.curr += 1
        return self.curr

    def __iter__(self):
        self.curr = self.start - 1
        return self


##############
# Generators #
##############

def generator():
    print("Starting here")
    i = 0
    while i < 6:
        print("Before yield")
        yield i
        print("After yield")
        i += 1

class IterGen:
    def __init__(self):
        self.start = 5

    def __iter__(self):
        while self.start < 10:
            self.start += 1
            yield self.start


def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    while n >= 0:
        yield n
        n -= 1

class Countdown:
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        while self.start >= 0:
            yield self.start
            self.start -= 1

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while n:
        yield n
        if n == 1:
            return n
        if n % 2:
            n = 3*n + 1
        else:
            n = n//2


