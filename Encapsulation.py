# Encapsulation is wrapping up of data under single unit.
# It's a shield that protects data from being accessed by the code outside the this shield

class Car():
    def __init__(self):
        self.make = "Toyota"
        self.model = "Noah"

ob = Car()
print(ob.make)
print(ob.model)
