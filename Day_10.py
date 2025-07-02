# Classes and objects |Inheritance
""" Class vs Object"""
""" Design / structure holo class
and implement hobar por view seta holo object.
"""
# class house_design():
#     print("design of 1 bhk house..")
#     no_of_window = 4
#     no_of_doors = 2
#
# my_real_house = house_design()
# print("my real house has-",my_real_house.no_of_window, "windows")
# print("my real house has-",my_real_house.no_of_doors,"doors")
#
# """Constructor"""
class tata_nano():
    def __init__(self,id_no,color,ac_type):
        self.id_no = id_no
        self.color = color
        self.ac_type = ac_type

    def display_color(self):
        print("color of",self.id_no,"-",self.color)
    def display_ac_type(self):
        print("AC_type of",self.id_no,"-",self.ac_type)

first_nano = tata_nano("M001","yellow","non-ac")
second_nano = tata_nano("M002","red","ac")

first_nano.display_color()
first_nano.display_ac_type()

second_nano.display_color()
second_nano.display_ac_type()

"Another class-object example"

class student():
    def __init__(self,name,roll_no,student_class):
        self.name = name
        self.roll_no = roll_no
        self.student_class = student_class

    def display(self):
        print("Name of the student is ",self.name)
        print("Roll no of the student is ", self.roll_no)
        print("Class of the student is",self.student_class)

s1=student("Raja", 1, 12)
s1.display()
print("\n")

s2=student("sukanta",2,12)
s2.display()
print("\n")

s3=student("rahul",3,10)
s3.display()


        
