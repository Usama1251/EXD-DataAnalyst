import os
import shutil

# cwd = os.getcwd()
# print("Current working directory: \n", cwd)

# os.chdir("C:\\Usama\Data Analyst")

# list1 = os.listdir(os.getcwd())
# print("Contents of directory", list1)

# os.mkdir("ANewDir")
# list2 = os.listdir(os.getcwd())
# print("Contents of Directory ", list2)

# os.rmdir('ANewDir')
# list3 = os.listdir(os.getcwd())
# print("Contents of directory ", list3)

#Task 1 to move folders to specific extension wle folders
path = os.path.abspath(r"C:\Usama\example")

for file in os.listdir(path):
    full_path = os.path.join(path, file)

    if os.path.isfile(full_path):
        extension = os.path.splitext(file)[1].lstrip(".")
        
        if extension == "":
            print("no folder")

        
        destinationFolder = os.path.join(path, extension.lstrip("."))
        if not os.path.exists(destinationFolder):
            os.mkdir(destinationFolder)

        shutil.move(full_path, os.path.join(destinationFolder, file))

    else:
        print('Already moved')





