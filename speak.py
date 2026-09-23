import os

# specify the directory path
path = "."

# get the list of files and directories    
contents = os.listdir()

# print the contents
print("Contents of directory:")
for item in contents:
    print(item)