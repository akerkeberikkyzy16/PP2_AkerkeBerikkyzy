#FUNCTION

#simple function without arguments
def say_hello():
    print("Hello! Welcome to Python.")
#function with one argument
def greet_user(name):
    print("Hello, " + name + "!")
#function that calculates the square of a number
def show_square(number):
    print(number * number)
#function that prints information
def show_student(name, age):
    print("Name:", name)
    print("Age:", age)
say_hello()
greet_user("Akerke")
show_square(5)
show_student("Akerke", 18)

#function with positional arguments
def introduce(name, city):
    print(name, "is from", city)
#function with a default argument
def greet(name, greeting="Hello"):
    print(greeting, name)
#function that receives a number
def check_age(age):
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are under 18.")
#function with two arguments
def add_numbers(first_number, second_number):
    print("Sum:", first_number + second_number)
introduce("Akerke", "Almaty")
greet("Akerke")
greet("Akerke", "Hi")
check_age(18)
add_numbers(10, 20)

#function that returns the sum of two numbers
def add(first_number, second_number):
    return first_number + second_number
#function that returns the square of a number
def square(number):
    return number * number
#function that returns True or False
def is_even(number):
    return number % 2 == 0
#function that returns the largest number
def find_largest(first_number, second_number):
    if first_number > second_number:
        return first_number
    return second_number
result = add(5, 10)
print("Sum:", result)
print("Square:", square(4))
print("Is 8 even?", is_even(8))
print("Largest number:", find_largest(15, 9))

#function using *args
def add_all_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    print("Total:", total)
#function using **kwargs
def show_information(**information):
    for key, value in information.items():
        print(key + ":", value)
#function using a normal argument and *args
def show_fruits(owner, *fruits):
    print("Owner:", owner)
    for fruit in fruits:
        print(fruit)
#function using default arguments and **kwargs
def create_profile(name, **details):
    print("Name:", name)
    for key, value in details.items():
        print(key + ":", value)
add_all_numbers(1, 2, 3, 4, 5)
show_information(name="Akerke", age=18, city="Almaty")
show_fruits("Akerke", "Apple", "Banana", "Orange")
create_profile("Akerke", university="KBTU", major="IT Management")



#LAMBDA

#basic lambda that adds two numbers
add = lambda first_number, second_number: first_number + second_number
print(add(5, 3))
#lambda that multiplies a number by 2
double = lambda number: number * 2
print(double(10))
#lambda that checks if a number is positive
is_positive = lambda number: number > 0
print(is_positive(7))
#lambda that returns the length of a word
word_length = lambda word: len(word)
print(word_length("Python"))

numbers = [1, 2, 3, 4, 5]
#map with lambda to create squares
squares = list(map(lambda number: number ** 2, numbers))
print("Squares:", squares)
#map with lambda to double numbers
doubled_numbers = list(map(lambda number: number * 2, numbers))
print("Doubled:", doubled_numbers)
#map with lambda to convert words to uppercase
words = ["python", "java", "c++"]
uppercase_words = list(map(lambda word: word.upper(), words))
print("Uppercase:", uppercase_words)
#map with lambda to add 10 to every number
increased_numbers = list(map(lambda number: number + 10, numbers))
print("Increased:", increased_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#filter with lambda to find even numbers
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", even_numbers)
#filter with lambda to find odd numbers
odd_numbers = list(filter(lambda number: number % 2 != 0, numbers))
print("Odd numbers:", odd_numbers)
#filter with lambda to find numbers greater than 5
greater_than_five = list(filter(lambda number: number > 5, numbers))
print("Greater than 5:", greater_than_five)
#filter with lambda to find positive numbers
mixed_numbers = [-5, -1, 0, 3, 7, -2]
positive_numbers = list(filter(lambda number: number > 0, mixed_numbers))
print("Positive numbers:", positive_numbers)

#list of names sorted by length
names = ["Anna", "Akerke", "Tom", "Alexander"]
sorted_names = sorted(names, key=lambda name: len(name))
print("Sorted by length:", sorted_names)
#list of numbers sorted in descending order
numbers = [5, 2, 9, 1, 7]
descending_numbers = sorted(numbers, key=lambda number: number, reverse=True)
print("Descending:", descending_numbers)
#list of students sorted by age
students = [
    ("Akerke", 18),
    ("Anna", 20),
    ("Tom", 19)
]
sorted_students = sorted(students, key=lambda student: student[1])
print("Sorted students:", sorted_students)
#list of words sorted alphabetically
words = ["banana", "apple", "orange", "grape"]
alphabetical_words = sorted(words, key=lambda word: word.lower())
print("Alphabetical:", alphabetical_words)


#CLASSES

#simple class definition
class Student:
    pass
student_one = Student()
student_two = Student()
print(student_one)
print(student_two)
#class with a class variable
class University:
    name = "KBTU"
university = University()
print("University:", university.name)
#simple class
class Car:
    brand = "Toyota"
    model = "Camry"
car = Car()
print("Brand:", car.brand)
print("Model:", car.model)
#adding an object property
class Person:
    pass
person = Person()
person.name = "Akerke"
print("Name:", person.name)

#class with an __init__ method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("Akerke", 18)
print("Name:", student.name)
print("Age:", student.age)
#class with three instance variables
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
book = Book("Python Basics", "John Smith", 2026)
print(book.title)
print(book.author)
print(book.year)
#class for a car
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
car = Car("Toyota", "Camry")
print(car.brand, car.model)
#class for a product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
product = Product("Laptop", 500000)
print("Product:", product.name)
print("Price:", product.price)

#class with an instance method
class Student:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("Hello, my name is", self.name)
student = Student("Akerke")
student.introduce()
#class with a method that changes a value
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        print("New balance:", self.balance)
account = BankAccount("Akerke", 1000)
account.deposit(500)
#class with a calculation method
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
rectangle = Rectangle(5, 4)
print("Area:", rectangle.calculate_area())
#class with a method that displays information
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_info(self):
        print("Phone:", self.brand, self.model)
phone = Phone("Apple", "iPhone 16")
phone.show_info()
#class variable shared by all objects
class Student:
    university = "KBTU"
    def __init__(self, name):
        self.name = name
student_one = Student("Akerke")
student_two = Student("Anna")
print(student_one.name, "-", student_one.university)
print(student_two.name, "-", student_two.university)
#change to an instance variable
student_one.name = "Akerke Berikkyzy"
print("Student one:", student_one.name)
print("Student two:", student_two.name)
#change to a class variable
Student.university = "New University"
print(student_one.university)
print(student_two.university)
#deleting an object property
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("Tom", 18)
del person.age
print("Name:", person.name)



#INHERITANCE

#parent class
class Animal:
    def eat(self):
        print("The animal is eating.")
#child class
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")
dog = Dog()
dog.eat()
dog.bark()
#inheritance example
class Vehicle:
    def move(self):
        print("The vehicle is moving.")
class Car(Vehicle):
    def drive(self):
        print("The car is driving.")
car = Car()
car.move()
car.drive()
#third inheritance example
class Person:
    def introduce(self):
        print("I am a person.")
class Student(Person):
    def study(self):
        print("The student is studying.")
student = Student()
student.introduce()
student.study()

#super() used to call the parent constructor
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university
student = Student("Akerke", "KBTU")
print("Name:", student.name)
print("University:", student.university)
#super()
class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name
class Dog(Animal):
    def __init__(self, animal_name, breed):
        super().__init__(animal_name)
        self.breed = breed
dog = Dog("Buddy", "Golden Retriever")
print("Name:", dog.animal_name)
print("Breed:", dog.breed)
#super() used to call a parent method
class Parent:
    def show_message(self):
        print("Message from parent.")
class Child(Parent):
    def show_parent_message(self):
        super().show_message()
child = Child()
child.show_parent_message()
#super() with a university example
class University:
    def __init__(self, university_name):
        self.university_name = university_name
class ITStudent(University):
    def __init__(self, university_name, major):
        super().__init__(university_name)
        self.major = major
it_student = ITStudent("KBTU", "IT Management")
print(it_student.university_name)
print(it_student.major)

#overriding with animals
class Animal:
    def make_sound(self):
        print("The animal makes a sound.")
class Dog(Animal):
    def make_sound(self):
        print("The dog says Woof!")
class Cat(Animal):
    def make_sound(self):
        print("The cat says Meow!")
animal = Animal()
dog = Dog()
cat = Cat()
animal.make_sound()
dog.make_sound()
cat.make_sound()
#overriding with vehicles
class Vehicle:
    def move(self):
        print("The vehicle moves.")
class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")
class Boat(Vehicle):
    def move(self):
        print("The boat moves on water.")
car = Car()
boat = Boat()
car.move()
boat.move()
#overriding with people
class Person:
    def introduce(self):
        print("I am a person.")
class Student(Person):
    def introduce(self):
        print("I am a student.")
student = Student()
student.introduce()
#overriding with shapes
class Shape:
    def get_name(self):
        return "Shape"
class Circle(Shape):
    def get_name(self):
        return "Circle"
circle = Circle()
print(circle.get_name())

#first parent class
class Camera:
    def take_photo(self):
        print("Taking a photo.")
#second parent class
class Phone:
    def make_call(self):
        print("Making a call.")
#child class using multiple inheritance
class Smartphone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the internet.")
smartphone = Smartphone()
smartphone.take_photo()
smartphone.make_call()
smartphone.browse_internet()
#multiple inheritance example
class Father:
    def father_skill(self):
        print("Father's skill.")
class Mother:
    def mother_skill(self):
        print("Mother's skill.")
class Child(Father, Mother):
    def child_skill(self):
        print("Child's skill.")
child = Child()
child.father_skill()
child.mother_skill()
child.child_skill()
#multiple inheritance
class Programmer:
    def code(self):
        print("Writing Python code.")
class Designer:
    def design(self):
        print("Creating a design.")
class ITSpecialist(Programmer, Designer):
    def work(self):
        print("Working in IT.")
specialist = ITSpecialist()
specialist.code()
specialist.design()
specialist.work()
#multiple inheritance example
class Musician:
    def play_music(self):
        print("Playing music.")
class Athlete:
    def play_sport(self):
        print("Playing sport.")
class TalentedPerson(Musician, Athlete):
    pass
person = TalentedPerson()
person.play_music()
person.play_sport()