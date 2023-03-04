import os

source = "Test.txt"
destination = "G:\\My Drive\\My Documents\\Misc\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already such a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
