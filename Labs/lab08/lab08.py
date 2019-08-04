## Linked Lists and Sets ##

# Linked Lists

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

def slice_link(link, start, end):
    """Slices a Link from start to end (as with a normal Python list).

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> slice_link(link, 1, 4)
    Link(1, Link(4, Link(1)))
    """
    # count = 0
    # while count < start:
    #     link = link.rest
    #     count += 1
    # new = Link(link.first)
    # new_begin = new
    # while count < end - 1:
    #     link = link.rest
    #     new.rest = Link(link.first)
    #     new = new.rest
    #     count += 1
    # return new_begin

    if link is Link.empty:
        return link
    if end <= 1:
        return Link.empty
    if start:
        return slice_link(link.rest, start - 1, end)
    if end:
        return Link(link.first, slice_link(link.rest, 0, end - 1))



# Sets

def union(s1, s2):
    """Returns the union of two sets.

    >>> r = {0, 6, 6}
    >>> s = {1, 2, 3, 4}
    >>> t = union(s, {1, 6})
    >>> t
    {1, 2, 3, 4, 6}
    >>> union(r, t)
    {0, 1, 2, 3, 4, 6}
    """
    for x in s2:
        if x not in s1:
            s1.add(x)
    return s1


def intersection(s1, s2):
    """Returns the intersection of two sets.

    >>> r = {0, 1, 4, 0}
    >>> s = {1, 2, 3, 4}
    >>> t = intersection(s, {3, 4, 2})
    >>> t
    {2, 3, 4}
    >>> intersection(r, t)
    {4}
    """
    new = set()
    for x in s1:
        if x in s2:
            new.add(x)
    return new

def extra_elem(a,b):
    """B contains every element in A, and has one additional member, find
    the additional member.

    >>> extra_elem(['dog', 'cat', 'monkey'],  ['dog',  'cat',  'monkey',  'giraffe'])
    'giraffe'
    >>> extra_elem([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
    6
    """
    a = set(a)
    b = set(b)
    for x in b:
        if x not in a:
            return x

def find_duplicates(lst):
    """Returns True if lst has any duplicates and False if it does not.

    >>> find_duplicates([1, 2, 3, 4, 5])
    False
    >>> find_duplicates([1, 2, 3, 4, 2])
    True
    """
    return len(lst) != len(set(lst))


