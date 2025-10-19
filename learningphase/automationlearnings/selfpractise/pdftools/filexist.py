import os

filename="drill1.txt"

if os.path.exists(filename):
    print("file exists")
else:
    print("file doesn't exist")