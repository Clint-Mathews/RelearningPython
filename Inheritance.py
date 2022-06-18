class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("No speak")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} color")


class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("tim", 10)
p.show()
c = Cat("Bill", 20,"Red")
c.show()
d = Dog("Jill",30)
d.show()
f = Fish("Bubbles",10)
f.show()

p.speak()
c.speak()
d.speak()
f.speak()