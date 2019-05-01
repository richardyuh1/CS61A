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
    "*** YOUR CODE HERE ***"
    i = n
    while i>=0:
        yield i
        i -= 1

def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    """
    assert len(s) >= k
    "*** YOUR CODE HERE ***"
    i = 0
    while i<k:
        yield s[i]
        i+=1
    raise ValueError





def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    t = iter(t)
    lastvalue = next(t)
    count = 1
    try:
        while True:
            value = next(t)
            if value == lastvalue:
                count += 1
                if count == k:
                    return value
            else:
                lastvalue = value
                count = 1

    except StopIteration:
        return None
    



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
    "*** YOUR CODE HERE ***"
    yield n
    if n == 1:
        return
    if n!=1:
        if n%2 == 0:
            n = n//2
            yield from hailstone(n)
        else:
            n = (3*n) + 1
            yield from hailstone(n)






