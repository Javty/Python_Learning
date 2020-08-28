# How to write to a file:
# Open the file in write mode
# Write to the file


def copy_files()
# Copy contents of one file to another
    with open("read.txt") as reader:
        with open("copy.txt") as copy:
            copy.write(reader.read())

def write_numbers(numbers):
    with open("file_numbers.txt", "w") as my_story:
        for number in range(numbers):
            if number % 2 == 0:
                my_story.write(f"{number}\n")

if __name__ == '__main__':
    write_numbers(31)
