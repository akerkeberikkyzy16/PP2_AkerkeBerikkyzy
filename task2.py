
# 1. BOOLEAN VALUES

is_student = True
is_tired = False

print(is_student)
print(is_tired)



# 2. BOOLEANS AS COMPARISON RESULTS


print(5 > 3)
print(10 < 4)
print(7 == 7)
print(5 != 5)
print(18 >= 18)



# 3. BOOLEAN OPERATORS


# AND
age = 20
print(age >= 18 and age <= 30)

# AND
is_student = True
has_id = True
print(is_student and has_id)

# OR
day = "Saturday"
print(day == "Saturday" or day == "Sunday")

# NOT
is_raining = False
print(not is_raining)

# OR
age = 16
has_permission = True
print(age >= 18 or has_permission)



# 4. IF STATEMENT


age = 20

if age >= 18:
    print("You are an adult")


temperature = 30

if temperature > 25:
    print("It is hot")


money = 1000

if money > 500:
    print("You can buy it")


password = "1234"

if password == "1234":
    print("Correct password")


score = 90

if score >= 90:
    print("Excellent!")



# 5. IF ELSE


age = 20

if age >= 18:
    print("Adult")
else:
    print("Child")


number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


password = "hello"

if password == "1234":
    print("Correct")
else:
    print("Wrong password")


temperature = 10

if temperature > 20:
    print("Warm")
else:
    print("Cold")


money = 500

if money >= 1000:
    print("You can buy it")
else:
    print("Not enough money")



# 6. IF ELIF ELSE


age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")


score = 75

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")


temperature = 15

if temperature > 25:
    print("Hot")
elif temperature > 10:
    print("Warm")
else:
    print("Cold")


number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


day = "Friday"

if day == "Monday":
    print("Start of week")
elif day == "Friday":
    print("Almost weekend")
else:
    print("Normal day")


# ==========================================
# 7. SHORT HAND IF ELSE
# ==========================================

age = 20

result = "Adult" if age >= 18 else "Child"
print(result)


number = 5

result = "Even" if number % 2 == 0 else "Odd"
print(result)


temperature = 30

message = "Hot" if temperature > 25 else "Cold"
print(message)


money = 1000

result = "Enough" if money >= 500 else "Not enough"
print(result)


password = "1234"

result = "Correct" if password == "1234" else "Wrong"
print(result)



# 8. SWITCH / IF ELIF ELSE




day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Unknown day")


operation = "+"

match operation:
    case "+":
        print("Addition")
    case "-":
        print("Subtraction")
    case "*":
        print("Multiplication")
    case "/":
        print("Division")


light = "red"

match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")


# IF / ELIF / ELSE version

day = "Monday"

if day == "Monday":
    print("School")
elif day == "Saturday":
    print("Weekend")
elif day == "Sunday":
    print("Weekend")
else:
    print("Normal day")


choice = 2

if choice == 1:
    print("Pizza")
elif choice == 2:
    print("Burger")
elif choice == 3:
    print("Pasta")
else:
    print("Unknown choice")



# 9. WHILE LOOPS


number = 1

while number <= 5:
    print(number)
    number += 1


count = 5

while count > 0:
    print(count)
    count -= 1


number = 2

while number <= 10:
    print(number)
    number += 2


x = 1

while x <= 3:
    print("Hello")
    x += 1


money = 100

while money > 0:
    print("Money left:", money)
    money -= 20



# 10. WHILE LOOP BREAK


number = 1

while number <= 10:
    print(number)

    if number == 5:
        break

    number += 1


# Example 2
while True:
    word = input("Enter quit: ")

    if word == "quit":
        break


# Example 3
number = 1

while number <= 10:
    if number == 7:
        break

    print(number)
    number += 1


# Example 4
x = 0

while x < 10:
    x += 1

    if x == 4:
        break

    print(x)


# Example 5
password = ""

while True:
    password = input("Password: ")

    if password == "1234":
        print("Correct!")
        break



# 11. WHILE LOOP CONTINUE


number = 0

while number < 10:
    number += 1

    if number % 2 == 0:
        continue

    print(number)


# Example 2
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)


# Example 3
number = 0

while number < 10:
    number += 1

    if number < 5:
        continue

    print(number)


# Example 4
x = 0

while x < 5:
    x += 1

    if x == 2:
        continue

    print("Number:", x)


# Example 5
number = 0

while number <= 10:
    number += 1

    if number % 2 != 0:
        continue

    print(number)



# 12. FOR LOOPS


for number in range(5):
    print(number)


for number in range(1, 6):
    print(number)


fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)


word = "Python"

for letter in word:
    print(letter)


for number in range(2, 11, 2):
    print(number)



# 13. FOR LOOP BREAK


for number in range(1, 10):

    if number == 5:
        break

    print(number)


# Example 2
for fruit in ["apple", "banana", "orange"]:

    if fruit == "banana":
        break

    print(fruit)


# Example 3
for number in range(10):

    if number == 7:
        break

    print(number)


# Example 4
for letter in "Python":

    if letter == "h":
        break

    print(letter)


# Example 5
for number in range(1, 101):

    if number > 10:
        break

    print(number)


# 14. FOR LOOP CONTINUE


# Example 1
for number in range(1, 10):

    if number % 2 == 0:
        continue

    print(number)


# Example 2
for number in range(1, 10):

    if number == 5:
        continue

    print(number)


# Example 3
word = "hello"

for letter in word:

    if letter in "aeiou":
        continue

    print(letter)


# Example 4
numbers = [-2, 5, -1, 8, 3]

for number in numbers:

    if number < 0:
        continue

    print(number)


# Example 5
for number in range(1, 11):

    if number % 3 == 0:
        continue

    print(number)