class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello my name is {self.name}. I am {self.age} years old."

    def describe(self):
        print("HI, This is ", self.name, ", And I am ", self.age)


p1 = Person('Abebe', 25)

# print(p1())
p1.describe()
