students = ["Akerke", "Dana", "Aliya"]
grades = [90, 85, 95]

#enumerate: get index and value
for index, student in enumerate(students):
    print(index, student)

#zip: combine two lists
for student, grade in zip(students, grades):
    print(student, grade)

#Convert a list to a tuple
students_tuple = tuple(students)
print(students_tuple)

#Convert a string to a list
letters = list("Python")
print(letters)

#Convert a number to a string
number = 100
text_number = str(number)
print(text_number, type(text_number))

#Convert a string to an integer
age = int("18")
print(age, type(age))

#Convert a string to a float
price = float("12.5")
print(price, type(price))

#Type checking
print(isinstance(age, int))
print(type(price))
