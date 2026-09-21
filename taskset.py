#PYTHON CLASSES
#getString and printString
class MyString:

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())


obj = MyString()

obj.getString()
obj.printString()

#square ingerits from shape
class Shape:

    def area(self):
        print(0)


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)


square = Square(5)
square.area()

#rectangle inhertis from shape
class Shape:

    def area(self):
        print(0)


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)


rectangle = Rectangle(5, 4)
rectangle.area()

#point class
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("x =", self.x)
        print("y =", self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()

point1.move(5, 5)
point1.show()

print("Distance:", point1.dist(point2))

#bank account
class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.balance)


account = Account("Akerke", 1000)

account.deposit(500)
account.deposit(200)

account.withdraw(300)
account.withdraw(2000)

#filter() lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)

#PYTHON FUNCTIONS
#grams ounces
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces


grams = float(input("Enter grams: "))

print("Ounces:", grams_to_ounces(grams))

#fahrenheit celsius
def fahrenheit_to_celsius(F):
    C = (5 / 9) * (F - 32)
    return C


F = float(input("Enter Fahrenheit: "))

print("Celsius:", fahrenheit_to_celsius(F))

#chickens and rabbits
def solve(numheads, numlegs):

    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits

    print("Chickens:", chickens)
    print("Rabbits:", rabbits)


solve(35, 94)

#filter_prime
def filter_prime(numbers):

    result = []

    for n in numbers:

        if n < 2:
            continue

        prime = True

        for i in range(2, n):

            if n % i == 0:
                prime = False
                break

        if prime:
            result.append(n)

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter_prime(numbers))

#all permutations of a string
from itertools import permutations


def all_permutations(text):

    result = permutations(text)

    for p in result:
        print("".join(p))


text = input("Enter a string: ")

all_permutations(text)

#reverse the words
def reverse_words(sentence):

    words = sentence.split()
    words.reverse()

    return " ".join(words)


sentence = input("Enter a sentence: ")

print(reverse_words(sentence))

#has_33
def has_33(nums):

    for i in range(len(nums) - 1):

        if nums[i] == 3 and nums[i + 1] == 3:
            return True

    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#spy_game
def spy_game(nums):

    code = [0, 0, 7]
    index = 0

    for number in nums:

        if number == code[index]:
            index += 1

            if index == 3:
                return True

    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#volume of a sphere
import math


def sphere_volume(radius):

    volume = (4 / 3) * math.pi * radius ** 3

    return volume


r = float(input("Enter radius: "))

print("Volume:", sphere_volume(r))

#unique elements without set
def unique_elements(numbers):

    result = []

    for number in numbers:

        if number not in result:
            result.append(number)

    return result


numbers = [1, 2, 2, 3, 4, 4, 5]

print(unique_elements(numbers))

#palindrome
def is_palindrome(text):

    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False


word = input("Enter a word: ")

print(is_palindrome(word))

#histogram
def histogram(numbers):

    for number in numbers:
        print("*" * number)


histogram([4, 9, 7])

#guess the number
import random


name = input("Hello! What is your name?\n")

number = random.randint(1, 20)

print()
print(name + ", I am thinking of a number between 1 and 20.")
print("Take a guess.")

guesses = 0

while True:

    guess = int(input())

    guesses += 1

    if guess < number:
        print("Your guess is too low.")
        print("Take a guess.")

    elif guess > number:
        print("Your guess is too high.")
        print("Take a guess.")

    else:
        print()
        print("Good job, " + name + "! You guessed my number in", guesses, "guesses!")
        break

#import functions from another file
#suppose function.py
def grams_to_ounces(grams):
    return 28.3495231 * grams


def sphere_volume(radius):
    import math
    return (4 / 3) * math.pi * radius ** 3
#then another file is main.py
from functions import grams_to_ounces, sphere_volume


print(grams_to_ounces(100))

print(sphere_volume(5))

#IMDB above 5.5
def is_good_movie(movie):

    if movie["imdb"] > 5.5:
        return True
    else:
        return False


print(is_good_movie(movies[0]))

#movies with IMDB above 5.5
def good_movies(movies):

    result = []

    for movie in movies:

        if movie["imdb"] > 5.5:
            result.append(movie)

    return result


print(good_movies(movies))

#movies from a specific category
def movies_by_category(movies, category):

    result = []

    for movie in movies:

        if movie["category"] == category:
            result.append(movie)

    return result


print(movies_by_category(movies, "Romance"))

#average IMDB score
def average_imdb(movies):

    total = 0

    for movie in movies:
        total += movie["imdb"]

    return total / len(movies)


print(average_imdb(movies))

#average IMDB score for a category
def average_category(movies, category):

    total = 0
    count = 0

    for movie in movies:

        if movie["category"] == category:
            total += movie["imdb"]
            count += 1

    if count == 0:
        return 0

    return total / count


print(average_category(movies, "Romance"))



