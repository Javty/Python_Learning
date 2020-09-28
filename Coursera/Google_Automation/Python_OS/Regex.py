import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[\d+\]"
result = re.search(regex, log)
print(result[0])

regex = r"aza"
result = re.search(regex, "plaza")

regex = r"^x"
result = re.search(regex, "xenon")
print(result[0])

regex = r"p.ng"
result = re.search(regex, "Pangaea")
print(result)
if result != None:
    print(result[0])

def search_regex(regex, word, casesensitive):
    if casesensitive is True:
        print(re.search(regex, word, re.IGNORECASE))
    else:
        print(re.search(regex, word))

regex = r"[a-z]way" #away
regex = r"cloud[A-Za-z0-9]"
regex = r="^P[^a]pa" # if ^is inside of Square brackets is like !=
regex = r"cat|dog" # is or
re.findall(r"cat|dog", "this cat is pretty and thi dog, cat too")
regex = r"Py.*n"
regex = r"Py[a-z]*n"
regex = r"o+l+" #e.g oooollll, oool, ollll
regex = r"o+[iI]l+"
regex = r"[Aa].*[Aa]" #annual
regex = r"p?each" #0 or 1 occurrence of character before it
regex = r"\.py"
regex = r"\w*" #Returns the first word
regex = r"\W*"
