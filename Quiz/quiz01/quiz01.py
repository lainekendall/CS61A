# CS 61A Fall 2014
# Name:
# Login:

def harmonic(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75


    """
    def rec(k):
        return 1/k
    return (2/(rec(x)+rec(y)))


from math import pi

def pi_fraction(k):
    """Print the fraction within gap of pi that has the smallest denominator.

    >>> pi_fraction(1)
    3 / 1 = 3.0
    >>> pi_fraction(0.01)
    22 / 7 = 3.142857142857143
    >>> pi_fraction(1/8)
    13 / 4 = 3.25
    >>> pi_fraction(1e-6)
    355 / 113 = 3.1415929203539825


    """
    numerator, denominator = 1, 1
    a = (numerator/denominator)
    b = pi - k
    c = pi + k
    while a<b or a>c:
        a = (numerator/denominator)
        b = pi - k
        c = pi + k
        if a>c:
            numerator = 1
            denominator +=1
        elif a<b:
            numerator += 1

    print(numerator, '/', denominator, '=', a)
        

def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0


    """
    if x >= 1:
        k = 0
        b = (pow(2,k))-(pow(2,k-1))+(pow(2,k-2))
        while b <= x:
            b = (pow(2,k))-(pow(2,k-1))+(pow(2,k-2))
            k += 1
        a = pow(2,k-2)
        c = 2*a
        return .5*c
    else:
        k = -1
        b = (pow(2,k))-(pow(2,k-1))+(pow(2,k-2))
        while b >= x:
            b = (pow(2,k))-(pow(2,k-1))+(pow(2,k-2))
            k -= 1
        a = pow(2,k+1)
        c = 2*a
        return .5*c

