# While loop -it execute numerous item as long as their  condition

count = 100
while count <= 105:
    print(count)
    count += 1

count = 100
while count <= 110:
    print(count)
    count += 2

number = 20
while number <= 25:
    print(number)
    number += 1

# Decrementing values
x = 10
while x >= 1:
    print(x)
    x -= 1
# Break statement
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1

# Skip statement and continue statement
y = 1
while y <= 6:
    y += 1
    if y == 4:
        continue
    print(y)

# For loop -  -help to display the content of variable
languages = ["python", "PHP", "kotlin", "java"]
for x in languages:
    print(x)

# Range numbers
for number in range(30, 40):
    print(number)

# if you don't specify the range it prints from 0 by default
for a in range(10):
    print(a)

for num in range(10, 20, 2):
    print(num)
