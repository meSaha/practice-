# Dictionary | If else Condition
# Dictionaries are used to store data values in key: value pairs.
# A dictionary is collection which is ordered*, Changeable and do not allow duplicates.

# get,keys,values,items
my_dict = {
    "Name": "Raja Saha",
    "Mode": "Online",
    "Profession": ["Python Developer", "SQL", "Power Bi"]
}

print(my_dict)
print(my_dict["Name"],my_dict["Profession"])
print(len(my_dict))
print(type(my_dict))
print(my_dict.get("Profession"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# Update existing value, Adding new key and value
info = {
    "Your_Name": "Sanjoy Saha",
    "Occupation": "Software Developer",
    "Skills": ["Android", "Kotlin","Java"]
}
print(info)
info["Occupation"]="SAP Developer"
print(info)
info["City"]= "Bangalore"
print(info)

# use for
my_bio = {
    "Emp_Code" : "RS-021991",
    "Company" : "SAP",
    "Designation" : "Software Developer",
    "Skills" : ["Django", "Fastapi", "Python"]
}
# for keys in my_bio:
#     print(keys)
# my_bio.update({"mode":"Hybrid"})
# print(my_bio)

# use pop,delete,
my_dicti = {
    "Name": "RDP",
    "t_s": 106,
    "subjects":["python","SQL","Power Bi"]
}
print(my_dicti)
print(my_dicti.pop("Name"))
my_dicti.popitem()
print(my_dicti)
del my_dicti
print(my_dicti) # NameError: name 'my_dicti' is not defined

# For loop
emp_details = {
    "Name": "RDP",
    "t_s": 106,
    "subjects":["python","Django"]
}
for keys in emp_details:
    print(keys)
    print(emp_details[keys])

for keys,values in emp_details.items():
    print(keys,":",values)


# Copying a dictionary
emp_details = {
    "Name": "RDP",
    "t_s": 106,
    "subjects":["python","Django"]
}
my_another_basket = emp_details
print(my_another_basket)

my_second_basket = emp_details.copy()
print(my_second_basket)

my_third_basket = dict(emp_details)
print(my_third_basket)

# Another examples
course_1 = {
    "course_name" : "python",
    "duration" : 4
}
course_2 = {
    "course_name" : "sql",
    "duration": 5
}
RDP_course = {
    "RDP_course_1" : course_1,
    "RDP_course_2" : course_2
}
print(RDP_course["RDP_course_1"]["course_name"])
print(RDP_course["RDP_course_2"]["duration"])

# if else
"""
Equals: a == b
Not Equals : a !=b
Less than: a < b 
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b 
"""

a = 50
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
