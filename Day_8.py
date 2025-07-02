def display():
    print("Hello...!!! Raja Saha")
display()

# addition
def add(a,b,c): # parameter or arguments
    print(a + b)
    print(a - b)
    print(c)

add(10, 20, 30)
add(100, 200, 600)

"Function calling"
def juice_machine():
    print("hello,ami Juice Machine theke bolchi...")

def RO_purifier(normal_water):
    print("hello dada RO purifier theke bolchi...")
    purified_water = "purified water"
    return purified_water

juice_machine()
purifier_er_jol = RO_purifier("normal_water")
print(purifier_er_jol)

"Function Arguments"
def addition(a,b):
    c = a + b
    print("Output of addition function :", c)
addition(3,6)

def addition(name,email):
    print("Your name-",name,"\n Your email-",email)
addition("Raja","coding123@gmail.com")

""""Number of Arguments"
def addition(name,email):
    print("Your name- ", name,"\n Your email-", email)
    addition("Rajdeep")"""""

# Arbitrary Arguments
def addition(*arguments):
    print(arguments)
    print(arguments[2])
    print(arguments[0])
addition("Rajdeep", "dar", "pathshala","156")

# keyword Arguments
def addition(a,b,c):
    print("a is ",a)
    print("b is ",b)
    print("c is ",c)
addition(10,20,30)

def addition(a,b,c):
    print("a is ",a)
    print("b is ",b)
    print("c is ",c)
addition(c = 10, a = 20, b =30)

"""Arbitrary Keyword Arguments, **kwargs"""
def addition(**parameters):
    print("your name -", parameters["name"])
    print("your job -", parameters["job"])
    print("your institution -", parameters["institution"])
addition(name="rajdeep", job="IT prof",institution="RDP")

"""Default parameter Value"""
def display(name = "Raja"):
    print(name)
# display()
display("PYTHON RDP")

"""Passing a List as an Argument"""
def display(list_param):
    for values in list_param:
        print(values)

my_list = ["ami", "python","sikhi",[1,2,3]]
display(my_list)

# Another example
print("hello...")
def add(a,b,c):
    pass
print("oops...")
