# class is the blueprint of an object
# objects are instances of a class

class Person:
    name = "Joe"
    age = 20
    gender = "male"
    def walk(self):
        print("walking")

p = Person()
p.walk()
print(p.name)