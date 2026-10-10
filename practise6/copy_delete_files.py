import shutil
from pathlib import Path

#Create a file
file_path = Path("original.txt")
file_path.write_text("This is my original file.", encoding="utf-8")

#Copy the file
shutil.copy("original.txt", "copy.txt")
print("File copied.")

#Create a backup
shutil.copy("original.txt", "backup.txt")
print("Backup created.")

#Check before deleting
if file_path.exists() and file_path.is_file():
    file_path.unlink()
    print("Original file deleted.")
else:
    print("File does not exist.")
