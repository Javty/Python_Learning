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
regex = r"^A.*a$"
regex = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
#groups
result = re.search(r"^(\w*), (\w*)", "lovelace, Ada")
result.groups() #str
result[0]

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

def rearrange_name2(name):
  result = re.search(r"^(\w* ?.*), (\w* ?.*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

regex = r"^([\w \.-]*), ([\w \.-]*)$"
regex = r"[A-Za-z]{5}"
regex = r"\b[A-Za-z]{5}\b"
regex = r"\w{5,10}"
regex = r"\w{5,}"
regex = r"s\w{,20}"
regex = r"\[(\d+)\]: ([A-Z]+)"

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex,log_line)
    if result is None:
        return ""
    return result[1]

log = "One sentence. Another one? And the last one!"
re.split(r"[\.?!]", log)
re.split(r"([\.?!])", log)
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
re.sub(r"^([\w .-]*), ([\w .-])$", r"\2 \1", "Lovelace, Ada")


def transform_record(record):
  new_record = re.sub(r"([\d-]+)", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer

def multi_vowel_words(text):
  pattern =  r"\w*[aeiou]{3}\w*"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))


def transform_comments(line_of_code):
  result = re.sub(r"#+", r"//", line_of_code)
  return result

print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"

def convert_phone_number(phone):
  result = re.sub(r" (\d{3})-(\d{3})", r" (\1) \2", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300
