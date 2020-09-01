favorites = {'color': 'purple', 'number': 42, 'animal': 'turtle', 'language': 'python'}
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for key in dictionary:
    print(key)

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for entry in dictionary.items():
    print(entry)

for key, value in favorites.items():
    print(f"my favorite {key} is {value}")

#split and count

str = 'it appears that the the appears the most in the sentence'
list = str.split(" ")
dict = {}
for word in list:
    if word in dict:
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1
for key, value in dict.items():
    print(f"\'{key}\' appears {value} time(s) in the string")

# Loop over list

foods = [['apple', 'banana', 'orange'],['carrot', 'cucumber', 'tomato']]

for e in foods:
    print(e)

for e in foods[0]:
    print(e)


# Loop Over dictionaries
pets = {
    'birds': {
        'parrot': 'Arthur',
        'canary': 'Ford'
    },
    'fish': {
        'goldfish': 'Zaphod',
        'koi': 'Trillium'
    }
}

for e in pets:
    print(e)
print("new for:")
for e in pets["birds"]:
    print(e)
print("new for:")
for e in pets["fish"]:
    print(e)
print("new for:")
for e in pets["birds"].values():
    print(e)


#list of dictionares
weather = [
    {
        'date':'today',
        'state': 'cloudy',
        'temp': 68.5
    },
    {
        'date':'tomorrow',
        'state': 'sunny',
        'temp': 74.8
    }
]

for e in weather[0].values():
    print(e)

for e in weather[0]:
    print(e)

for e in weather:
    print(e['date'])
    print(e['state'])
    print(e['temp'])

for e in weather:
    print(e['date'])
    print(e['state'])
    print(e['temp'])

for forecast in weather:
    print(forecast['date'])
    print(forecast['state'])
    print(forecast['temp'])

#for forecast in weather:
#    print('The weather for ' + forecast['date'] + ' will be ' + forecast['state'] + ' with a temperature of ' + str(forecast['temp']) + ' degrees.')

for forecast in weather:
    print(f"The weather for {forecast['date']} will be {forecast['state']} with a temperature of {forecast['temp']} degrees.")

for forecast in weather:
    date = forecast['date']
    state = forecast['state']
    temp = forecast['temp']
    print(f"The weather for {date} will be {state} with a temperature of {temp} degrees.")
