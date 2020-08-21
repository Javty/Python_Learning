#Given list of strings, return the count of duplicate strings.
# ["apple","orange","orange","banana", "apple,"orange"] -> ["apple":2, "orange":3, "banana":1]

fruit = ["apple", "orange" ,"orange" ,"banana" ,"apple", "orange"]
def fruit_list (fruit):
    n=0
    list2 = []
    for x in range(len(fruit)):
        if fruit[x] not in list2:
            list2.append(fruit[x])
            count_fruits(fruit,list2[n])
            n= n + 1

def count_fruits(string, target):
    count = 0
    for component in string:
        if component == target:
            count = count + 1
    return print (target,":",count)

fruit_list(fruit)
