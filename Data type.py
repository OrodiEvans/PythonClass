# Datatype
number = 100  # integer
second = 56.78  # float
text = "hello there"  # string
isinteresting = True  # bool
cars = ["Toyota", "Nissan", "vw"]  # list ...we use special brackets
fruits = ("Banana", "Orange", "Apple")  # tuple
countries = {"Kenya", "Rwanda", "Uganda"}  # set
details = {
    "firstname": "Evans",
    "lastname": "Orodi",
    "age": 30,
    "course": "MIT",
    "nationality": "Kenyan"
}  # Dictionary
print(details)
print(details["course"])
print(cars)
print(fruits)
print(countries)
print(number)
print(second)
# to ignore a particular part use # before the line of code.

print(number)
print(second)
print(number, "is an integer")

# Determining data type
print(type(number))
print(type(second))
print(type(isinteresting))

# Typecasting - converting one data type into another
print(float(number))
print(int(second))
print(str(number))
