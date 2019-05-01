###########
# Mobiles #
###########

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    return root(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return tree(None, [tree(size)])

def size(w):
    """Select the size of a weight."""
    "*** YOUR CODE HERE ***"
    return root(branches(w)[0])

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    "*** YOUR CODE HERE ***"
    if len(branches(w)) == 1:
        return True
    else:
        return False


def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    [left,right] = sides(m)
    
    if total_weight(end(left)) * length(left) == total_weight(end(right)) * length(right):
        if is_weight(end(left)) and is_weight(end(right)):
            return True
        elif is_weight(end(left)) == False and is_weight(end(right)):
            return balanced(end(left))
        elif is_weight(end(left)) and is_weight(end(right)) == False:
            return balanced(end(right))
        else:
            return balanced(end(left)) and balanced(end(right))
    else:
        return False




def with_totals(m):
    """Return a mobile with total weights stored as the root of each mobile.

    >>> t, _, v = examples()
    >>> root(with_totals(t))
    3
    >>> print(root(t))                           # t should not change
    None
    >>> root(with_totals(v))
    9
    >>> [root(end(s)) for s in sides(with_totals(v))]
    [3, 6]
    >>> [root(end(s)) for s in sides(v)]         # v should not change
    [None, None]
    """
    "*** YOUR CODE HERE ***"

    [left,right] = sides(m)
    
    if is_weight(end(left)) and is_weight(end(right)):
        return tree(total_weight(m),[left,right])
    elif is_weight(end(left)) and is_weight(end(right)) == False:
        return tree(total_weight(m), [left,side(length(right),with_totals(end(right)))])
    elif is_weight(end(left)) == False and is_weight(end(right)):
        return tree(total_weight(m), [side(length(left),with_totals(end(left))),right])
    else:
        return tree(total_weight(m),[side(length(left), with_totals(end(left))),side(length(right), with_totals(end(right)))])


############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"
    list = []
    def withdraw(amount, stringpass):
        nonlocal balance
        nonlocal password
        nonlocal list
        if len(list) >= 3:
            return 'Your account is locked. Attempts: [\'{0}\', \'{1}\', \'{2}\']'.format(list[0], list[1], list[2])
        elif stringpass != password:
            list.append(stringpass)
            return 'Incorrect password'
        elif amount > balance:
            return 'Insufficient funds'
        else:
            balance = balance - amount
            return balance
    return withdraw

validwords = []
count = 0

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    global count
    
    if count >=3:
        return withdraw(0,old_password)

    if type(withdraw(0, old_password)) == str:
        count += 1
        return 'Incorrect password'
    
    
    validwords.append(old_password)
    validwords.append(new_password)

    def withdraw_new(amount, string):
        global count
        
        if type(withdraw(0,old_password)) == int:
            balance = withdraw(0,old_password)

        if string in validwords:
            return withdraw(amount, old_password)
        else:
            count += 1
            return withdraw(amount,string)


    return withdraw_new





