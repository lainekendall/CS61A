## Extra Linked Lists and Sets ##

from lab08 import *

# Set Practice

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to any n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    """

    sums = set()
    lst = set(lst)
    for x in lst:
        if n-x != x:
            sums.add(n-x)
    if lst.intersection(sums):
        return True
    return False

def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    >>> pow(2,7)
    128
    >>> pow(2,8)
    256
    >>> pow(2,4)
    16
    """
    if k == 0:
        return 1
    if k % 2:
        return n * pow(n,k-1)
    return pow(n*n,k/2)

def missing_no(lst):
    """lst contains all the numbers from 1 to n for some n except some
    number k. Find k.

    >>> missing_no([1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> missing_no(list(filter(lambda x: x != 293, list(range(2000)))))
    293
    """
    n = max(lst)
    lst = set(lst)
    for x in range(n):
        if x not in lst:
            return x

def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    # >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    # False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    """
    # short = list(set(lst))
    # print(short)  #find duplicates...
    # num = extra_elem(short,lst)
    # print(num)
    # if not num:
    #     return False
    # start = lst.index(num) + 1 
    # for x in range(start,len(lst-k)):
    #     copy = lst[x:x+k + 1]
    #     if num in copy:
    #         return True
    # return False



    copy = lst[:]
    temp = copy[0:k+1]
    for start in range(len(lst)-k+1): # 0 to length - k
        if len(temp) != len(set(temp)):
            return True
        temp = copy[start:start + k+1]
    return False




