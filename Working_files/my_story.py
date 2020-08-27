#print(f"Hello world {variable}")
def check(story):
    rude_words = ["feo", "chiquito", "hola", "que", "hace"]
with open("my_story.txt") as my_story:
    contents = my_story.read()
    rude_count = 0
    for rude in rude_words:
        if rude in contents:
            rude_count += 1
        print(f"found rude word: {rude}")
if rude_count == 0:
    print("Congratulations, your file has no rude words.")
    print("At least, no rude words I know.")
else:
    print(f"you have {rude_count} rude words")

if __name__ == '__main__':
    check("my_story.txt")
