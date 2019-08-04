def read_tail(src):
    """Return the remainder of a list in SRC, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([")"])))
    nil
    >>> read_tail(Buffer(tokenize_lines(["2 3)"])))
    Pair(2, Pair(3, nil))
    >>> read_tail(Buffer(tokenize_lines(["2 (3 4))"])))
    Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
    >>> read_line("(1 . 2)")
    Pair(1, 2)
    >>> read_line("(1 2 . 3)")
    Pair(1, Pair(2, 3))
    >>> read_line("(1 . 2 3)")
    Traceback (most recent call last):
        ...
    SyntaxError: Expected one element after .
    >>> scheme_read(Buffer(tokenize_lines(["(1", "2 .", "'(3 4))", "4"])))
    Pair(1, Pair(2, Pair('quote', Pair(Pair(3, Pair(4, nil)), nil))))
    """
    try:
        if src.current() is None:
            raise SyntaxError("unexpected end of file")
        elif src.current() == ")":
            src.pop()
            return nil
        elif src.current() == ".":
            "*** YOUR CODE HERE ***"
            src.pop()          
            val = scheme_read(src)
            if src.current() != ")":
                raise SyntaxError("Expected one element after .")
            else:
                src.pop()
                return val
        else:
            first = scheme_read(src)
            rest = read_tail(src)
            return Pair(first, rest)

    except EOFError:
        raise SyntaxError("unexpected end of file")