# Local Variable | Global Variable 
"""A variable created inside a function belongs to the scope of that function,
and can only be used inside that function."""

# Local Scope
# def outer():
#     number = 100
#     print(number)
# outer()
# print(number)

# def outer():
#     number = 100
#     def inner():
#         print(number*30)
#     inner()
#     print(number)
#
# outer()
# #


# Global Scope
main_number = 1000
def outer():
    number = 100
    def inner():
        inner_number = 250
        print(number*30)
        print(inner_number)
        print(main_number)
    inner()
    print(number)
    print(main_number)

# Global variable
def outer():
    global number
    number = 200
    print(number)

    def inner():
        print(number)
    inner()
outer()
print(number)

