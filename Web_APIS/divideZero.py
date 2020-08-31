import requests

x = int(input("Enter a Number:"))
try:
    print (3/x)
except ZeroDivisionError:
    print("Can´t divide by zero")

def name_Error():
    try:
        x = y + 1
    except NameError:
        x = 0
    print(x)

try:
    r = requests.get(url)
    print(r.text)
except requests.exceptions.ConnectionError:
    print("could not connecto to server!")

try:
    r = requests.get("https://www.udacity.com")
except NameError:
    print("did you forget to import the module")

try:
    print(r.text)
except NameError:
    print("There seems to be a NameError; r is not defined!")

string = 'short'
try:
    for letter in range(6):
        print(string[letter])
except IndexError:
    print("Did you try to index past the end of the string?")
