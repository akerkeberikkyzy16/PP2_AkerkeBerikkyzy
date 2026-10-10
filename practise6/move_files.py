import shutil
from pathlib import Path

#Create source and destination directories
source_folder = Path("source")
destination_folder = Path("destination")

source_folder.mkdir(exist_ok=True)
destination_folder.mkdir(exist_ok=True)

#Create a sample file
file_path = source_folder / "example.txt"
file_path.write_text("Hello!", encoding="utf-8")

#Copy the file to another directory
shutil.copy2(
    str(file_path),
    str(destination_folder / "example.txt")
)

print("File copied.")

#Move the file to another directory
shutil.move(
    str(file_path),
    str(destination_folder / "moved_example.txt")
)

print("File moved.")
