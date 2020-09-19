import os
import string

def check_file(file):
    with open(file) as file: #with (name, "w") as new_file:
        check = []
        for line in file:
            message = line.split()
            message = "".join(message) + ".wav"
            if message in check:
                i = message.find(".")
                x = message[i-1]
                if x.isnumeric():
                    x = int(x)
                    x += 1
                    message = message[:i] + str(x) + message[i:]
                else:
                    message = message[:i] + "1" + message[i:]
            check.append(message)
            print(message)#new_file.write(message)
#check_file("Work.txt")

def write_template(name, templates, combinations):
    with open(name, "w") as options:
        for template in templates:
            for combination in combinations:
                options.write(f"{combination}{template}\n")

if __name__ == '__main__':
    check_file("check.txt")
