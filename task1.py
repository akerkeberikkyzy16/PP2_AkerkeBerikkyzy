#print("Hello World")
print("this will work")
print(3)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = "awesome"
def myfunc():
  y = "!!!"
  print("Python is " + x +y)
myfunc()

type()

x = "Hello World" #str
x=20 #int
x=20.5 #float
x=1j #complex
x = ["apple", "banana", "cherry"] #list
x = ("apple", "banana", "cherry")	#tuple
x=range(6) #range
x = {"name" : "John", "age" : 36}	#dict
x = {"apple", "banana", "cherry"} #set
x = frozenset({"apple", "banana", "cherry"}) #frozenset
x=True #bool
x=None #NoneType

b = "Hello, World!"
print(b[2:5])
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."

print(10 > 9)
print(10 == 9)
print(10 < 9)

num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)

x = 5
print(x > 0 and x < 10)

x = 5
print(x < 5 or x > 10)

x = 5
print(not(x > 3 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)