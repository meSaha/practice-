# Polymorphism
class virat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def batting(self):
        print(self.name, "is great in batting")
    def bowling(self):
        print(self.name, "is not so good bolwer")

class bumra:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def batting(self):
        print(self.name, "is not so good in batting")
    def bowling(self):
        print(self.name, "is a great bolwer")

Virat_Kohli = virat("Virat Kohli", 35)
Jasprit_Bumra = bumra("Jasprit Bumra", 29)

Virat_Kohli.batting()
Virat_Kohli.bowling()

Jasprit_Bumra.batting()
Jasprit_Bumra.bowling()
