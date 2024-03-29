## Extra Recursive Objects ##

from lab07 import *

# Linked List Practice

def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> list_to_link([1, 2, 3])
    Link(1, Link(2, Link(3)))
    """
    def helper(lst, link):
        if not lst:
            return link
        else:
            link = Link(lst[-1], link)
        return helper(lst[0:-1], link)
    return helper(lst, ())




    # lst = lst[0:-1]
    # for x in len(lst):

    # w = ()
    # w = Link(w)
    # w = lst[last]
    # return Link(w)

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    def helper(link, lst):
        if link is Link.empty:
            return lst
        else:
            lst.append(link.first)
        return helper(link.rest, lst)
    return helper(link, [])

def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> reverse(Link(1))
    Link(1)
    >>> link = Link(1, Link(2, Link(3)))
    >>> reverse(link)
    Link(3, Link(2, Link(1)))
    >>> link
    Link(1, Link(2, Link(3)))
    """
    def helper(link, new):
        if link is Link.empty:
            return new
        elif len(link) == 1:
            return Link(link.first, new)
        else:
            new = Link(link.first, new)
            return helper(link.rest, new)
    return helper(link, ())


def mutate_reverse(link):
    """Mutates the Link so that its elements are reversed.

    >>> link = Link(1)
    >>> mutate_reverse(link)
    >>> link
    Link(1)

    >>> link = Link(1, Link(2, Link(3)))
    >>> mutate_reverse(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    def helper(link, l):
        if not l:
            return
        else:

            return helper(link.rest, l-1)
    return helper(link, len(link))


# Tree Practice

def leaves(t):
    """Returns a list of all the entries of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    def helper(t, lst):
        if t.is_leaf():
            lst.append(t.entry)
        else:
            for branch in t.branches:
                helper(branch, lst)
        return lst
    return helper(t, [])

def cumulative_sum(t):
    """Return a new Tree, where each entry is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    "*** YOUR CODE HERE ***"
    def sum_entries(t):
        if t.is_leaf():
            return t.entry
        else:
            return t.entry + sum([sum_entries(branch) for branch in t.branches])


    if t.is_leaf():
        return Tree(sum_entries(t))
    else: 
        return Tree(sum_entries(t), [cumulative_sum(branch) for branch in t.branches])


    # else:
    #     # return Tree(cumulative_sum(branch), )
    #     for branch in t.branches:
    #         t.entry = cumulative_sum(branch)



def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape if they have the same number of branches and each of their
    children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = cumulative_sum(t)
    >>> same_shape(t, s)
    True
    """
    "*** YOUR CODE HERE ***"
    if t1.is_leaf() or t2.is_leaf():
        return t1.is_leaf() and t2.is_leaf()
    else:
        for branch1, branch2 in t1.branches, t2.branches:
            return len(t1.branches) == len(t2.branches) and same_shape(branch1, branch2)



# Folding Linked Lists

from operator import add, sub, mul

def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    fn(z, link.first)
    return foldl(link.rest, fn, link.first)

def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"

identity = lambda x: x

def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"
    return foldr(link, step, identity)(z)

