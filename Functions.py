#  1. User defined functions
def greeting():
    print("hello world")


greeting()  # calling a function


def add():
    print(7 + 8)


add()


# Parameters and arguments
def employee(fullname, age, position, salary):
    print(fullname, age, position, salary)


employee("Faith Dye", 30, "Manager", 50000)
employee("John Major", 50, "Sergent", 100000)

# 2. Built-in library functions
y = max(56, 79, 32, 16, 90)

print(y)

x = min(20, 56, 100, 40, 90)
print(x)

z = pow(2, 3)
print(z)

