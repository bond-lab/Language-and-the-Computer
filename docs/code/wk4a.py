# a bilingual dictionary!

en2cs = {
    "list": "seznam",
    "set": "množina",
    "boolean": "booleovská hodnota",
    "tuple": "ntice",
    "dictionary": "slovník",
    "string": "řetězec" }

for en, cs in en2cs.items():
    print(f'{en} = {cs}')
print()

# reverse!
cs2en = dict()
for en, cs in en2cs.items():
    cs2en[cs] = en

for cs, en in cs2en.items():
    print(f'{cs} = {en}')
print()

    
### Food

print('\nDictionary of Dictionaries')
food = { 'bread': {'ingredients': ['flour', 'yeast', 'water', 'salt'],
                   'prep time': '30 min',
                   'cook time': '40 min',
                   'comments': 'nice with whole grains'
                   },
         'jam': {'ingredients': ['strawberry', 'apple', 'sugar'],
                 'prep time': '15 min',
                 'cook time': '30 min',
                 'comments': '',
                },
         'temaki sushi': {'ingredients': ['rice', 'sushi vinegar', 'fish'],
                          'prep time': '45 min',
                          'cook time': '',
                          'comments': 'also need soy sauce to eat',
                          },
         }

###
### Note: I do not expect you to check for empty strings
###       I just wanted to show that it can be done.
###

for f in food:
    print(f'{f.title()}')
    fd = food[f]
    print ('Ingredients:')
    for i in fd['ingredients']:
        print (f'    {i}')
    if {fd['cook time']}: # assume there is always prep time
        print (f"Prep/Cook time: {fd['prep time']}/{fd['cook time']}")
    else:
        print (f"Prep time: {fd['prep time']}")        
    if fd['comments']:
        print (f"Comments: {fd['comments']}")
    print()


# Ask the user how many languages they speak
num_languages = input("How many languages do you speak? ")
num_languages = int(num_languages)
    
# Determine the response based on the number of languages
if num_languages == 1:
    print("You should study more!")
elif 2 <= num_languages <= 3:
    print("Good!")
elif num_languages > 3:
    print("Well done!")
print()

