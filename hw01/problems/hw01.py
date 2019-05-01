from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        return a - b
    else:
        return a + b


def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    large1 = 0
    large2 = 0
    if a == b:
        large1 = a
        large2 = max(a,c)
    if a>c:
        if a>b:
            large1 = a
            large2 = max(b,c)
        else:
            large1 = b
            large2 = a
    if c>a:
        if c>b:
            large1 = c
            large2 = max(a,b)
        else:
            large1 = b
            large2 = c
    return (large1*large1) + (large2*large2)




def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    maxfactor = 1
    for num in range(1,n):
        if n%num == 0:
            if num > maxfactor:
                maxfactor = num
    return maxfactor



def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    global x
    x = 0
    return False

def t():
    "*** YOUR CODE HERE ***"
    global x
    x += 1
    return x

def f():
    "*** YOUR CODE HERE ***"
    global x
    x += 1
    return x

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 0

    while n!=1:
        print(n)
        count += 1
        if n%2 == 0:
            n = n//2
        else:
            n = (n*3)+1
    print(n)
    return count+1


