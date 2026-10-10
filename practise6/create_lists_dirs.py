import os
from pathlib import Path

#Create a directory
Path("PracticeFolder").mkdir(exist_ok=True)

#Create nested directories
Path("PracticeFolder/Folder1/Folder2").mkdir(parents=True, exist_ok=True)

#Show current directory
print("Current directory:", os.getcwd())

#List all items
print("All items:", os.listdir("."))

#List only files and directories
path = Path(".")

print("Files:")
for item in path.iterdir():
    if item.is_file():
        print(item.name)

print("Directories:")
for item in path.iterdir():
    if item.is_dir():
        print(item.name)

#Find files with a specific extension
print("Python files:")
for item in path.iterdir():
    if item.is_file() and item.suffix == ".py":
        print(item.name)

#Change current directory
#os.chdir("PracticeFolder")
#print(os.getcwd())
#Remove an empty directory
#os.rmdir("EmptyFolder")
