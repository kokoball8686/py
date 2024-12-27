

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print('hello', self.name)
        print('I am %s years old' % self.age)


p1 = Person('Chan', 28)
print(p1.name, p1.age)
p1.myfun()