###
#### Prompt the user to enter a series of foods until they enter 'quit'
###

food = 'food'
while food.lower() != 'quit':
    food = input("Enter a food to cook for the party (or type 'quit' to stop): ")
    if food.lower() != 'quit':
        print(f"I'll cook {food} for the party!")
print()

active = True
while active:
    food = input("Enter a food to cook for the party (or type 'quit' to stop): ")
    if food.lower() == 'quit':
        active = False
    else:
        print(f"I'll cook {food} for the party!")
print()

while True:
    food = input("Enter a food to cook for the party (or type 'quit' to stop): ")
    if food.lower() == 'quit':
        break
    print(f"I'll cook {food} for the party!")
print()

###
### set and more 
###

print('\nCounting tokens\n')

tokens = [
    "Holmes", "had", "been", "seated", "for", "some", "hours", "in", "silence",
    "with", "his", "long", ",", "thin", "back", "curved", "over", "a", "chemical",
    "vessel", "in", "which", "he", "was", "brewing", "a", "particularly",
    "malodorous", "product", ".", "His", "head", "was", "sunk", "upon", "his",
    "breast", ",", "and", "he", "looked", "from", "my", "point", "of", "view",
    "like", "a", "strange", ",", "lank", "bird", ",", "with", "dull", "gray",
    "plumage", "and", "a", "black", "top-knot", "." ]

print(f'There are {len(tokens)} tokens')
print(f'There are {len(set(tokens))} different tokens')

print(f'There are {len([w.lower() for w in tokens])} lower case tokens')
print(f'There are {len(set([w.lower() for w in tokens]))} different lower case tokens')


freq = dict()

for w in tokens:
    if w.lower() in freq:
        freq[w.lower()] += 1
        # or freq[w.lower()] = freq[w.lower()] + 1
    else:
        freq[w.lower()] = 1
###
### The first version is more Pythonic because it leverages the ability to iterate 
### directly over dictionary items, resulting in cleaner, more efficient, and more
### readable code.
###
for w, f in freq.items():
    if f > 1:
        print(f'{f}\t{w}')
print()

for w in freq:
    if freq[w] > 1:
        print(f'{freq[w]}\t{w}')
print()
#Just for fun
for w, f in freq.items():
    print(f"{'*' * f}\t({w})")

### remove stop words

print('\nFiltering Lists\n')

stop = ['.', ',', ';', 'a', 'an', 'of', 'the', 'he', 'his', 'him', 'me', 'my', 'I', 'you', 'your', 'we', 'our', 'us']
clean = []

for t in tokens:
    if t.lower() not in stop:
        clean.append(t)

print ('Tokens with out stop words:', clean)
print()
##
## or use list comprehension
##

print ('Tokens with out stop words:', [t for t in tokens if t.lower() not in stop])
print()
