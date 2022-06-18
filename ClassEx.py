class Person:
    def __init__(self,name):
        self.name = name

    def updateName(self,name):
        self.name = name

    def hello(self,x):
        return x+1;
    def printName(self):
        print(self.name)

p = Person("Clins")
p2 = Person("Clint")
print(type(p))
p.printName()
p2.printName()

print(p.hello(12))
print(p2.hello(14))

p.updateName("CLins1")
p2.updateName("CLint1")

p.printName()
p2.printName()