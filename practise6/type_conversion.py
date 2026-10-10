#Different data types
number = 10
decimal = 3.14
text = "25"
is_student = True

#Type checking
print(type(number))
print(type(decimal))
print(type(text))
print(type(is_student))

#Type conversion
print(float(number))
print(int(decimal))
print(int(text))
print(str(number))
print(bool(number))

#Convert a string into a list of characters
print(list("Hello"))

#Convert a list into a tuple
print(tuple([1, 2, 3]))

#Convert a list of pairs into a dictionary
pairs = [("name", "Akerke"), ("age", 18)]
print(dict(pairs))
