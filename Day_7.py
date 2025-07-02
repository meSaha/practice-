
# while loop  | for loop
"""Equals: a == b
    Not Equals : a !=b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b """
i = 0
while i < 6:
    print("value if i is ", i)
    i = i+1

# 1 ki 6 er theke choto 1 < 6 (less than)
# 6 ki 6 er theke choto 6 < 6 (soman tai condition stop hoye jbe)

my_list = [1, 2, 3, 4]
while len(my_list)>0:
    print(my_list)
    my_list.pop()

# 0 theke len ta joto khon boro thakbe
# 1 > 0 theke boro (greater than 1 > 0:
# 3 ki 0 theke boro ( 3 > 0)

""" The While Loop-Infinite Loop """
# Jor kore condition True korchi.so eta infinite loop.
# if conditional statement.
while True:
    user_input = input("Enter 'q' to quit:")
    if user_input == 'q':
        break # Exit the loop if the user enters 'q'
    else:
        print("You didn't enter 'q'.")

" The While Loop-Break,condition and Else "
count = 0
while count < 5: # joto khon count er value 5er theke choto thakbe toto khon loop cholbe.
    if count == 2:
      count += 1
      continue # Skip iteration when count is 2
    print(count)
    if count == 3:
        break # Exit the loop iteration when count is 3
    count += 1

"The While Loop-Else condition"
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("The while loop has finished")

"The For Loop"
# for variable in sequence:
    # code to be executed

fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)

basket = ["python", "Javascript", "Php"]
for program in basket:
    print(program)

# Iterating

print(range(5))
print(type(range(5)))
for i in range (4,6):
    print(i)

# Iterating over a String
text = "python"
for char in text:
    print(char)

# Iterating over a dictionary
person = {"name":"John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)

my_dict ={"name":"jhon","age":30, "city":"New york"}
for key, value in my_dict.items():
    print(key,":", value)

for i in range (0,10,2): # start,stop,step
    print(i)


# enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruits)

# Nested Loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        for element in row:
            print(element," ", end= '')
