import json


#JSON string
student_json = '{"name": "Akerke", "age": 18, "university": "KBTU"}'

print(student_json)


#converting JSON to a Python dictionary
student_json = '{"name": "Akerke", "age": 18}'

student = json.loads(student_json)

print("Name:", student["name"])
print("Age:", student["age"])


#converting a Python dictionary to JSON
student = {
    "name": "Akerke",
    "age": 18,
    "major": "IT Management"
}

student_json = json.dumps(student)

print(student_json)


# Here is an example of writing JSON data to a file
student = {
    "name": "Akerke",
    "age": 18,
    "university": "KBTU"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file was created.")


#reading JSON data from a file
with open("student.json", "r") as file:
    student_data = json.load(file)

print("Name:", student_data["name"])
print("University:", student_data["university"])