# check the index of string
message = "cats & dogs"
message.index("&")


def remplace(message, old, new):
    while old in message:
        change = message.index(old)
        message = message[:change] + new + message[change+1:]
    return message


def remplace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


Email_list = ["javier@hotmail.com", "lourdes@hotmail.com", "lupita@gmail.com", "Sara@gmail.com", "Estefania@hotmail.com"]
count = 0
for email in Email_list:
    Email_list[count] = remplace_domain(email, "hotmail.com", "gmail.com")
    count += 1


user_input = " Yes  "
if user_input.lower().strip() == "yes":
    print("The user said yes")


message2 = "hello my friend how are you"


#method .endswith("rest"), is for ask if something end in do_something
message2.endswith("you")

#method .isnumeric(), return if the string is numeric



#Returns the initials of a words

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


#Formating expressions https://docs.python.org/3/library/string.html#format-specification-mini-language

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for chr in input_string.lower().strip():
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if chr != " ":
			reverse_string = chr + reverse_string
			new_string = new_string + chr
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

def nametag(first_name, last_name):
	return("{} {:.1s}.".format(first_name, last_name))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the
		# end with the new string
		i = len(old)
		new_sentence = sentence[:-i] + new
		return new_sentence

	# Return the original sentence if there is no match
	return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"



def get_word(sentence, n):
	# Only proceed if n is positive
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing



def skip_elements(elements):
	new_list = []
	i = 0
	for element in elements:
		if i % 2 == 0:
			new_list.append(element)
		i += 1
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

#this use enumerate for the index
def skip_elements(elements):
	new_list = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			new_list.append(element)

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

def skip_elements(elements):
    skip_element = [ number for number in elements if len(number) % 2 == 0]


List_tuples = [("roberto@gmail.com" , "Javier"), ("terra@hotmail.com", "juan")]

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


languages = ["Python", "Pearl", "Ruby", "Go", "Java", "C", "Javscript"]
lenghts = [len(x) for x in languages]

z = [x for x in range(1,101) if x % 3 == 0]


#Given list of strings, return the count of duplicate strings.
# ["apple","orange","orange","banana", "apple,"orange"] -> ["apple":2, "orange":3, "banana":1]

fruits = ["apple", "orange", "orange", "banana", "apple", "orange" ]
def Count_dic(fruits):
    reference = set(fruits)
    dic = {}
    for fruit in reference:
        dic[fruit] = fruits.count(fruit)
    return dic
