# Inheritance
class Father():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Father's name-", self.name)
        print("Father's age-", self.age)

class Son(Father):
    def __init__(self,name,age):
        self.son_name = name
        self.son_age = age
        super().__init__("Somnath",66)
    def show(self):
        print("son's name-", self.son_name)
        print("son's age-", self.son_age)

Rajendra_Singha = Father("Rajendra Singh",58)
Rajendra_Singha.display()

rahul = Son("rahul", 10)
rahul.show()
print(rahul.son_name)
print(rahul.son_age)

rahul.display()
print(rahul.name)
print(rahul.age)




