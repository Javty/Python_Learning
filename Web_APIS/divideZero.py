x = int(input("Enter a Number:"))
try:
    print (3/x)
except ZeroDivisionError:
    print("Can´t divide by zero")
