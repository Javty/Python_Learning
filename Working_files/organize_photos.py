import os

# 1. Get a list of the file names
os.chdir("Photos")
originals = os.listdir()
print(originals)
# 2. Extract the place names from the file names
# 3. Make a directory for each place name
# 4. Move files into the right directories
# os.mkdir = mkdir touch, os.listdir = ls, os.rename = mv
# os.getcwd() = pwd, os.chdir = cd, os.path.join() = os.path.join("Documents", "Photos", "Oahu") = 'Documents/Photos/Oahu'
