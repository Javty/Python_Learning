# os.mkdir = mkdir touch, os.listdir = ls, os.rename = mv
# os.getcwd() = pwd, os.chdir = cd, os.path.join() = os.path.join("Documents", "Photos", "Oahu") = 'Documents/Photos/Oahu'
# string operations filename.count("_"), boolean "_" in filename filename.find("_"), filename[::]
# Split "banana".split("n") = ["ba","a","a"]

import os

# 1. Get a list of the file names
os.chdir("Photos")
originals = os.listdir()
print(originals)
# 2. Extract the place names from the file names e.g "2016-11-04_Berlin_09/42/22.jpg"
def extract_place(filename):
    first = filename.find("_")
    partial = filename[first+1:]
    first = partial.find("_")
    final = partial[:first]
    return final

def extract_place2(filename):
    list = filename.split("_")
    return list[1]

def extract_place3(filename):
    return filename.split("_")[1]

print("Result: " ,extract_place("2016-11-04_Berlin_09/42/22.jpg"))
print("Result: " ,extract_place2("2016-11-04_Berlin_09/42/22.jpg"))
print("Result: " ,extract_place3("2016-11-04_Berlin_09/42/22.jpg"))
# 3. Make a directory for each place name
originals2=[]
for x in range(len(originals)):
    originals2.append(extract_place3(originals[x]))

print(originals2)

# 4. Move files into the right directories
