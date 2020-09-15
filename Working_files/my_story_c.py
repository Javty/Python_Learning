#print(f"Hello world {variable}")
import string
rude_words = ["fea", "tonta", "feas", "que", "hace"]

def check_line(line):
    rude_count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation)
        if word.lower() in rude_words:
            rude_count += 1
            print(f"Encontre una Palabra Grosera: {word}")
    return rude_count

def check_file(story):
    with open(story) as my_story:
        rude_count = 0
        for line in my_story:
                rude_count += check_line(line)

    if rude_count == 0:
        print("Felicidades, Tu no tienes groserias.")
        print("Al menos, groserias que no conozco.")
    else:
        print(f"Tu tienes {rude_count} groserias")

if __name__ == '__main__':
    check_file("my_story.txt")
