from lab11 import * 

###########
# Streams #
###########

class Stream:
    class empty:
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)

def add_streams(s1, s2):
    def helper():
        return add_streams(s1.rest, s2.rest)
    return Stream(s1.first + s2.first, helper)

def make_fib_stream():
    prev = 0
    curr = 1
    def helper():
        yield prev
        prev, curr = curr, prev + curr
    return Stream(helper(), helper)


    def helper(prev=0, curr=1):
        prev, curr = curr, prev + curr
        return [prev, curr]
    try:
        prev, curr = (helper(prev, curr))[0], (helper(prev, curr))[1]
    except NameError:
        prev = (helper())[0]
        curr = (helper())[1]
    return Stream(prev, make_fib_stream)

def filter_stream(filter_func, stream):
    def make_filtered_rest():
        return filter_stream(filter_func, stream.rest)
    if Stream.empty:
        return stream
    elif filter_func(stream.first):
        return Stream(stream.first, make_filtered_rest)
    else:
        return filter_stream(filter_funct, stream.rest)

def find(stream, predicate):
    "*** YOUR CODE HERE ***"

def interleave(stream1, stream2):
    "*** YOUR CODE HERE ***"

