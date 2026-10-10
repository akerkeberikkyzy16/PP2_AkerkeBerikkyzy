import os
from pathlib import Path

path = Path("sample.txt")

#Check if the path exists
print("Exists:", path.exists())

#Check access permissions
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

#Find filename and directory
if path.exists():
    print("Filename:", path.name)
    print("Directory:", path.parent)

# Count lines in a file
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

#Generate 26 text files: A.txt to Z.txt
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open(letter + ".txt", "w", encoding="utf-8") as file:
        file.write("This is file " + letter)

print("26 files created.")

#Copy the contents of one file to another
with open("sample.txt", "r", encoding="utf-8") as source:
    content = source.read()

with open("sample_copy.txt", "w", encoding="utf-8") as destination:
    destination.write(content)

print("Contents copied.")
