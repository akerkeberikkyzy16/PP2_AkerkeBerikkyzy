#TASK1
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

b = " Hello, World!"
print(b[2:5])
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("H", "J"))
print(b.split(","))

age = 36
txt = f"My name is John, I am {age}"
print(txt)

num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is y)


#TASK2

temperature = 15

if temperature > 25:
    print("Hot")
elif temperature > 10:
    print("Warm")
else:
    print("Cold")

age = 20
result = "Adult" if age >= 18 else "Child"
print(result)

#day = 1
#match day:
    #case 1:
        #print("Monday")
    #case 2:
        #print("Tuesday")
    #case 3:
        #print("Wednesday")
    #case _:
        #print("Unknown day")

number=9
while number <= 10:
    print(number)
    if number == 5:
        break
    number += 1

for number in range(5):
    print(number)


#TASK3

#function with one argument
def greet_user(name):
    print("Hello, " + name + "!")
greet_user("Akerke")

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

add = lambda first_number, second_number: first_number + second_number
print(add(5, 3))

#map(function, iterated_object)
numbers=[2,3,4]
squares = list(map(lambda number: number ** 2, numbers))
print("Squares:", squares)

#list of names sorted by length
names = ["Anna", "Akerke", "Tom", "Alexander"]
sorted_names = sorted(names, key=lambda name: len(name))
print("Sorted by length:", sorted_names)

#list of students sorted by age
students = [
    ("Akerke", 18),
    ("Anna", 20),
    ("Tom", 19)
]
sorted_students = sorted(students, key=lambda student: student[1])
print("Sorted students:", sorted_students)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("Akerke", 18)
print("Name:", student.name)
print("Age:", student.age)

#class with an instance method
class Student:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("Hello, my name is", self.name)
student = Student("Akerke")
student.introduce()

#class variable shared by all objects
class Student:
    university = "KBTU"
    def __init__(self, name):
        self.name = name
student_one = Student("Akerke")
student_two = Student("Anna")
print(student_one.name, "-", student_one.university)
print(student_two.name, "-", student_two.university)

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

#TASKSET
