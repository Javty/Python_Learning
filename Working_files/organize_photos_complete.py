import os


def organize_photos(directory):
    # 1. Get a list of the file names
    os.chdir(directory)
    originals = os.listdir()
    places = []
    # 2. Extract the place names from the file names
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)
            # 3. Make a directory for each place name
    make_directories(places)
    # 4. Move files into the right directories
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


def extract_place(filename):
    return filename.split("_")[1]


def make_directories(place):
    for x in place:
        os.mkdir(x)


if __name__ == '__main__':
    organize_photos("Photos")
