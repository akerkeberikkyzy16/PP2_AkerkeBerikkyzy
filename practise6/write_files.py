#Write data to a file
with open("students.txt", "w") as file:
    file.write("Akerke\n")
    file.write("Dana\n")

#Append new data
with open("students.txt", "a") as file:
    file.write("Aliya\n")

#Read and print the result
with open("students.txt", "r") as file:
    print(file.read())

#Write a list to a file
students = ["Akerke", "Dana", "Aliya"]

with open("student_list.txt", "w") as file:
    for student in students:
        file.write(student + "\n")
