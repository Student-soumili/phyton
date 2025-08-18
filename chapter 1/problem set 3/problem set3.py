import pyttsx3
engine = pyttsx3.init()

engine.say("meowwwwwww")
engine.runAndWait()

#4
import os

# Get the path of the directory you want to list
# Use '.' for the current directory or provide an absolute path
directory_path = '.'  # Change to any directory path you want

# Check if the directory exists
if os.path.isdir(directory_path):
    print(f"Contents of directory '{os.path.abspath(directory_path)}':\n")
    
    # Get and print the list of files and subdirectories
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            print(f"File:      {item}")
        elif os.path.isdir(item_path):
            print(f"Directory: {item}")
        else:
            print(f"Other:     {item}")
else:
    print(f"The path '{directory_path}' is not a valid directory.")
