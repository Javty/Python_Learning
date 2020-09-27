#!/usr/bin/env python3
import os
import datetime

with open("real.txt", "w") as files:
    for i in range(1,11):
        files.write(str(i)+"real")
#Rename a file
os.rename("real.txt","noWay.txt")
#remove a file
os.remove("noWay.txt")
#Check if a file exists
os.path.exists("alan.txt")
#Get the size of a file
os.path.getsize("alan.txt")
#Get the time of a file
os.path.getmtime("alan.txt")
#convert the time to somethin that can be readeable
timestamp = os.path.getmtime("alan.txt")
datetime.datetime.fromtimestamp(timestamp)
#Check if it is a file
os.path.isfile("alan.txt")
#Check the route
os.path.abspath("alan.txt")
#Get the current directory path
os.getcwd()
#Create a directory
os.mkdir()
#Change of directory
os.chdir()
#rdmir is for to remove a directory
os.rmdir()
# Get a list
os.listdir()


dir = "Test"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")


import os
def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
        path = os.getcwd()
        fullname = os.path.join(path, file)
        filesize = os.path.getsize(fullname)
    return filesize
