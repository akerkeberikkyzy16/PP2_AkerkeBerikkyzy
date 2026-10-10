#Sample file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is Practice 6.\n")
    file.write("We are learning file handling.\n")

#Read the whole file
with open("sample.txt", "r") as file:
    print("Using read():")
    print(file.read())

#Read the first line
with open("sample.txt", "r") as file:
    print("Using readline():")
    print(file.readline())

#Read all lines into a list
with open("sample.txt", "r") as file:
    print("Using readlines():")
    print(file.readlines())
