# parent class
class Animal:
    def walk(self):
        print("Animal is walking")
    def speak(self):
        print("Animal is speaking")

# child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")
d = Dog()
d.bark()
d.walk()

c = Cat()
c.meow()