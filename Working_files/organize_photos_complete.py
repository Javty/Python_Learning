import os
# 1. Get a list of the file names
os.chdir("Photos")
originals = os.listdir()
places=[]
# 2. Extract the place names from the file names

def extract_place3(filename):
    return filename.split("_")[1]

# 3. Make a directory for each place name

def make_directories(place):
    for x in place:
        os.mkdir(x)



for x in range(len(originals)):
    place = extract_place3(originals[x])
    if place not in places:
        places.append(place)

make_directories(places)
print(os.listdir())

# 4. Move files into the right directories
