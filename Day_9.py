""" Lambda Functions | Map and Lambda Function"""
from traceback import print_tb


def add (a):
    return a+10

result = add(10)
print(result)

# lambda example:
"""syntax
lambda arguments: expression
f = lambda a: a*a
f is a object that accepts and stores the result of the expression.
a * a => is one-line expression"""
x = lambda a :  a + 10
print(x(10))

""" Multiple Arguments in Lambda"""
x = lambda a,b : a * b
print(x(10,56))

my_number = lambda a,b,c : a+b+c
print(my_number(10, 20, 30))

""" Lambda with in Regular Function"""
def multiplier(n):
    return lambda x: x * n
# return lambda function
# double = lambda x: x * 2
double = multiplier(2)
result = double(5)
print(result)

# another example:
def myfunc(n):
    print(n)
    return lambda a: a * n
my_doubler = myfunc(2)
print(my_doubler(11))


""" Python map() Function| map(function, sequence)"""
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x : x ** 2, numbers))
print(squared)

""" Python filter() | filter(function, sequence)"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

