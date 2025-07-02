"""#### Day: 1 ####
# Assignment 1: Area of a Circle Write a program that calculates the area
# of a circle given its radius. The formula for the area of a circle is:
# Area = π * radius^2.
print("This application will  calculate the area of a circle")
radius = float(input("Please enter the radius of your circle:"))
pi = 3.14
area = pi*(radius*radius)
print("Area of your circle is", area)
print("Area of your circle is %0.2f" %area)

# Assignment 2: Temperature Conversion Write a program
# that converts temperature in Fahrenheit to Celsius.
# The formula is: Celsius = (Fahrenheit - 32) * 5/9.
# Take Fahrenheit from user.
print("This application will convert Temperature from Fahrenheit to Celsius.")
Fahrenheit = float(input("Please enter the Temperature in Fahrenheit: "))
Celsius = (Fahrenheit - 32) * 5/9
print("Temperature in celsius is ", Celsius)
print("Temperature in celsius is % 0.3f"% Celsius)
"""

""" ***Assignment 3***: Variable swap write a program that takes
two integer inputs from the user and swaps their values without using a
temporary variable."""

# "Method-1"
variable_1 = int(input("Please enter first value -"))
variable_2 = int(input("Please enter second value -"))
variable_1, variable_2 = variable_2, variable_1
print("result after swapping--")
print("Your first value is", variable_1, "and your second variable is ", variable_2)

# "Method-2"
variable_1 = int(input("please enter first value - "))
variable_2 = int(input("pLease enter second value -"))
variable_1 = variable_1 + variable_2
variable_2 = variable_1 - variable_2
variable_1 = variable_1 - variable_2
print("result after swapping--")
print("Your first value is", variable_1, "and your second variable is ", variable_2)

""" *** Assignment 4 ***:
Simple Interest Calculator Write a program that
calculates the simple interest for a given principal amount,
rate of interest, and time period. The formula for simple interest is:
Simple Interest = (principal * rate * time) / 100.
Take principal ,rate , time from user."""

print("This application is to create Simple Interest-")
principle = float(input("Please enter principle amount : "))
rate = float(input("Please enter Rate of interest in % :"))
time = int(input("PLease enter time in year:"))
interest = (principle * rate * time) /100
print("Your simple interest is ",interest)
print("Your simple interest is %0.3f" % interest)



""" ***Assignment 5 ***:
String Reversal Write a program that
takes a string as input and prints its reverse.
Example - user gave “Rajdeep”, your output will be “peedjaR” """

print("This is a string reversal program - ")
given_string = input("Please enter your name : ")
reversed_string = given_string[: : -1]
print("Your name is reverse ", reversed_string)


""" ***Assignment 6***:
User Information Write a program that takes
the user's name, age, and favorite color as inputs and then'
'prints them in a formatted message."""

print("This is a string formatting application - ")
name = input("Please enter your full name : ")
age = int(input("Please enter your age:"))
favourite_color = input("please enter your favourite color: ")
print("Hi", name, ".I can see your age is ",age," and your favourite color is", favourite_color)

""" ***Assignment 7***: 
Odd or Even Checker Write a program that
takes an integer input from the user and determines whether it's odd or even."""

print("This program is to find a number is ood or even - ")
your_number = int(input("Please enter your number: "))
if your_number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd")



""" ***Assignment 8***: 
Shopping Cart Total Write a program that
simulates a shopping cart. Prompt the user to enter the prices of
items they want to buy. After they're done, calculate and print the
'total cost of all the items in the cart'"""

print("Shopping Cart Total--- ")
t_shirt_price = float(input("Please enter the price of T-shirt: "))
t_shirt_quantity = int(input("How many T-shirts you bought: "))
saree_price = float (input("Please enter the price of Saree: "))
saree_quantity = float(input("How many Sarees you bought: "))
print("Your Subtotal is: ",(t_shirt_price*t_shirt_quantity)+(saree_price*saree_quantity))

""" ***Assignment 9***:
Character Count Write a program that takes a
string as input and counts the number of occurrences of a
specific character entered by the user."""

print("Character Count program - ")
sentence = input("Please enter a sentence: ")
specific_character = input("Please enter a specific_character which you want to find: ")
print("Number of occurrences",sentence.count(specific_character))

""" ***Assignment 10***: 
Name Initials Write a program that takes a
full name as input and outputs the initials in uppercase.
For example, if the input is "John Doe", the output should be "JD"."""

print("Name Initials program - ")
full_name = input("Please enter your full name : ")
name_in_title_format = full_name.title()
index_of_space = name_in_title_format.find(" ")
name_initials = name_in_title_format[0] + name_in_title_format[index_of_space +1]
print("Hello ", name_initials,"!!")


""" ***Assignment 11***: 
String Manipulation Basics Create a Python program that takes a user's
full name as input and prints it in reverse order (last name, first name).
Then, count and display the total number of characters in the full name.
Finally, extract and display the initials of the first and last names."""

print("String Manipulation Program : ")
full_name = input("Please enter your full name : ")
index_of_space = full_name.find(" ")
first_name = full_name[:index_of_space]
last_name = full_name[index_of_space + 1:]
print("your name is reverse order",last_name, first_name)
print("Total number of characters ",len(full_name))
full_name_in_title_format = full_name.title()
print("Initials of your name is", full_name_in_title_format[0]+full_name_in_title_format[index_of_space+1])


""" ***Assignment 12***: String Searching and Replacing:
Given a text containing a sample paragraph of text.
Write a Python program that reads this paragraph and searches for a
“specific word” and display the number of occurrence of that word.
Replace all occurrences of the word with “replace with”
word and display the modified text."""







""" Assignment 18:
Build a program that simulates a simple access.
# Control system. Prompt the user for a username and password.
# Then, use logical operators (and, or, not) to determine whether
# the user should be granted access or denied access based on
# predefined username and password criteria. Provide appropriate
# feedback to the user."""
print("login simulator -")
username = input("please set your username: ")
password = input("please set your password: ")

username_enter = input("Please enter your username: ")
password_enter = input("please enter your password: ")
if username ==username_enter and password == password_enter:
    print("Login Success full")
else:
    print("Please try again...")


