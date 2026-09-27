import math
import random


#using min and max
numbers = [10, 5, 20, 3, 15]

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))


#using abs, round, and pow
number = -15.7

print("Absolute value:", abs(number))
print("Rounded value:", round(number))
print("Power:", pow(2, 3))


#using math functions
number = 25

print("Square root:", math.sqrt(number))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))


#using pi, e, sin, and cos
print("Pi:", math.pi)
print("Euler's number:", math.e)
print("Sin:", math.sin(math.pi / 2))
print("Cos:", math.cos(0))


#using random functions
numbers = [1, 2, 3, 4, 5]

random_number = random.random()
random_integer = random.randint(1, 100)
random_item = random.choice(numbers)

print("Random number:", random_number)
print("Random integer:", random_integer)
print("Random item:", random_item)


#shuffling a list
names = ["Akerke", "Anna", "Tom", "Alex"]

random.shuffle(names)

print("Shuffled names:", names)