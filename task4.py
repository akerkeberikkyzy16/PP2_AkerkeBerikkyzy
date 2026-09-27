#GENERATORS
#generator that generates squares up to N
def generate_squares(n):
    for number in range(n + 1):
        yield number ** 2


n = int(input("Enter N: "))

for square in generate_squares(n):
    print(square)


#generator that prints even numbers from 0 to N
def generate_even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number


n = int(input("Enter N: "))

even_numbers = generate_even_numbers(n)

print(",".join(str(number) for number in even_numbers))


#generator that finds numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    for number in range(n + 1):
        if number % 3 == 0 and number % 4 == 0:
            yield number


n = int(input("Enter N: "))

for number in divisible_by_3_and_4(n):
    print(number)


#generator that yields squares from A to B
def squares(a, b):
    for number in range(a, b + 1):
        yield number ** 2


a = int(input("Enter A: "))
b = int(input("Enter B: "))

for square in squares(a, b):
    print(square)


#generator that returns numbers from N down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter N: "))

for number in countdown(n):
    print(number)


#DATA
from datetime import datetime, timedelta


#program that subtracts five days from the current date
current_date = datetime.now()

five_days_ago = current_date - timedelta(days=5)

print("Current date:", current_date)
print("Five days ago:", five_days_ago)


#program that prints yesterday, today, and tomorrow
today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())


#program that removes microseconds from datetime
current_datetime = datetime.now()

without_microseconds = current_datetime.replace(microsecond=0)

print("With microseconds:", current_datetime)
print("Without microseconds:", without_microseconds)


#program that calculates the difference between two dates in seconds
first_date = datetime(2026, 9, 20, 10, 0, 0)
second_date = datetime(2026, 9, 21, 12, 0, 0)

difference = second_date - first_date

difference_in_seconds = difference.total_seconds()

print("Difference in seconds:", difference_in_seconds)


#MATH
import math


#program that converts degrees to radians
degree = float(input("Input degree: "))

radian = math.radians(degree)

print("Output radian:", radian)


#program that calculates the area of a trapezoid
height = float(input("Height: "))
base_one = float(input("Base, first value: "))
base_two = float(input("Base, second value: "))

area = ((base_one + base_two) / 2) * height

print("Expected Output:", area)


#program that calculates the area of a regular polygon
number_of_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = (number_of_sides * side_length ** 2) / (
    4 * math.tan(math.pi / number_of_sides)
)

print("The area of the polygon is:", area)


#program that calculates the area of a parallelogram
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)


#JSON
import json


#program that opens the sample JSON file
with open("sample-data.json", "r") as file:
    data = json.load(file)


#program that prints the interface status table
print("Interface Status")
print("=" * 80)

print(
    "{:<50} {:<20} {:<8} {:<6}".format(
        "DN",
        "Description",
        "Speed",
        "MTU"
    )
)

print(
    "{:<50} {:<20} {:<8} {:<6}".format(
        "-" * 50,
        "-" * 20,
        "-" * 6,
        "-" * 6
    )
)


#loop that reads each interface from the JSON data
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")

    print(
        "{:<50} {:<20} {:<8} {:<6}".format(
            dn,
            description,
            speed,
            mtu
        )
    )