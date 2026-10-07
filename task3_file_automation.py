# CodeAlpha Python Internship
# Task 3 - File Automation
# This program moves all JPG files from one folder to another.


# Import the os module.
# It helps us work with folders and files.
import os

# Import the shutil module.
# It helps us move files from one location to another.
import shutil


# -----------------------------------------
# STEP 1: Define the folder names
# -----------------------------------------

# This is the folder where our JPG files are currently stored.
source_folder = "Source_Folder"

# This is the folder where we want to move the JPG files.
destination_folder = "Destination_Folder"


# -----------------------------------------
# STEP 2: Create destination folder
# -----------------------------------------

# Check whether the destination folder already exists.
if not os.path.exists(destination_folder):

    # If it does not exist, create it.
    os.makedirs(destination_folder)


# -----------------------------------------
# STEP 3: Get all files from Source_Folder
# -----------------------------------------

# Get the names of everything inside Source_Folder.
files = os.listdir(source_folder)


# -----------------------------------------
# STEP 4: Check every file
# -----------------------------------------

for file in files:

    # Check whether the file name ends with .jpg
    if file.lower().endswith(".jpg"):

        # Create the complete location of the source file.
        source_path = os.path.join(source_folder, file)

        # Create the complete location of the destination file.
        destination_path = os.path.join(destination_folder, file)

        # Move the JPG file to the destination folder.
        shutil.move(source_path, destination_path)

        # Tell the user which file was moved.
        print(file, "moved successfully.")


# -----------------------------------------
# STEP 5: Display final message
# -----------------------------------------

print("\nAll JPG files have been processed.")
print("Task completed successfully!")