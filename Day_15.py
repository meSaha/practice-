# Python Try Except | Math in Python | Module
# Math in python
a = min(5, 10, 25)
b = max(5, 10, 25)
c = abs(-7.25)
d = pow(4, 3)
print(a, b, c, d)

# Math Module
import math
a = math.sqrt(66)
b = math.ceil(1.4)
c = math.floor(1.4)
d = math.pi
print(a,"-->",b,"-->",c,"-->",d)

# try
"""The try block lets you test a block of code for errors."""

# except
"""The Except block lets you handle the error."""

# else
"The else block lets you execute code when there is no error."

# finally
"The finally block lets you execute code, regardless of the result of try-and except blocks."

# Example : 1
try:
    print(x)
except:
    print("Tested exception occurred")

# Example: 2
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("Something else went wrong")

# Example: 3
try:
    print(x)
except:
    print("something went Wrong")
finally:
    print("The try except is finished")
