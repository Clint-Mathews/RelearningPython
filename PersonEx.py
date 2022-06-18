class Person:
    num_of_people = 0
    GRAVITY = 9.8
    # Class attribute will not change for instances and will be same for all instance.
    # Can also be referenced using class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.add_people()

    # Class methods does not require access to the instances. It does not access any specific instance.
    # Just the class instance
    @classmethod
    def get_num_of_people(cls):
        return cls.num_of_people

    @classmethod
    def add_people(cls):
        cls.num_of_people += 1

p1 = Person("Clint",12)
print(Person.get_num_of_people())
p2 = Person("Clins",13)
print(Person.get_num_of_people())


Person.num_of_people = 30
p1.num_of_people = 20 # wrong case
print(p1.num_of_people)
print(p2.num_of_people)
print(Person.num_of_people)