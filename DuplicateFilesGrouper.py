"""
this program will scan item in a file and if 2 item with the same name it will group them together in a file
"""

import os
import shutil

working_directory = os.getcwd() + "\\File to work on"  # Get current directory and add directory called file to work on
# working directory is the file to run the program in

os.chdir(working_directory)  # tell the program to change the directory
print("cwd: " + os.getcwd() + "\n")  # prints out CWD

for item in sorted(os.listdir(working_directory)):  # loop each item in directory
    name, form = os.path.splitext(item)  # split the name and format separately
    file_name = [x.split('.')[0] for x in os.listdir(working_directory)]  # Create list of file names without extension

    if name.find(" - Copy") >= 0:
        print(name + " ---> is a copy found")
        copy_file = name[0:name.find(" - Copy")]  # get the file name without " - Copy"
        try:
            os.mkdir(copy_file)  # create a file
            print("Directory: ", copy_file, "  ---> Created ")
        except FileExistsError:
            print("Directory: ", copy_file, "  ---> already exists")
        shutil.move(working_directory + "\\" + name + form,  # move the item into file
                    working_directory + "\\" + copy_file + "\\" + name + form)
        print(name + "  ---> moved to folder\n")

    elif name.find(" - Copy") == -1 and file_name.count(name) >= 2:
        print(name + "  ---> is a duplicate found")
        try:
            os.mkdir(name)
            print("Directory: ", name, "  ---> Created ")
        except FileExistsError:
            print("Directory: ", name, "  ---> already exists")
        shutil.move(working_directory + "\\" + name + form, working_directory + "\\" + name + "\\" + name + form)
        print(name + "  ---> moved to folder\n")

    else:
        print(name + "  ---> only has one\n")
