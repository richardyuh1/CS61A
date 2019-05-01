class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """

    def __init__(self):
        self.value = 0

    def next(self):
        "*** YOUR CODE HERE ***"
        #create the next node in the linked list
        self.nextThing = Fib()
        
        #base case
        if self.value == 0:
            self.nextThing.value = 1
        
        #other wise the new nodes value = the previous nodes value + my value
        else:
            self.nextThing.value  = self.previous.value + self.value
        
        #the new nodes previous is myself
        self.nextThing.previous = self

        #return the next node
        return self.nextThing
    
        
    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.balance = 0
        self.quantity = 0
    def vend(self):
        if self.quantity == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.price:
            difference = self.price - self.balance
            return 'You must deposit $' + str(difference) + ' more.'
        elif self.balance == self.price:
            self.balance = 0
            self.quantity -= 1
            return 'Here is your ' + self.name + '.'
        else:
            a = self.balance
            self.balance = 0
            self.quantity -= 1
            return 'Here is your ' + self.name + ' and $' + str(a - self.price) + ' change.'

    def deposit(self, amount):
        self.balance += amount
        if self.quantity == 0:
            return 'Machine is out of stock. Here is your $' + str(amount) + '.'
        else:
            return 'Current balance: $' + str(self.balance)

    def restock(self, num):
        self.quantity += num
        return 'Current ' + self.name + ' stock:' + ' ' + str(self.quantity)



class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        "*** YOUR CODE HERE ***"
        if message.startswith(magic_word):
            command = ''
            command += message[7:]
            if hasattr(self.obj, command):
                return getattr(self.obj,command)(*args)
            else:
                return 'Thanks for asking, but I know not how to ' + command + '.'


