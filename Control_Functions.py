import random

number = random.randint(-10, 10)
if number < 0:
    print("negative")
elif number == 0:
    print("zero")
else:
    print("positive")
print(number)
