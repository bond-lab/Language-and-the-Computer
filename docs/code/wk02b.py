print('\nWierd Shape\n')

for i in range(1, 7):
    print('*' * i)
for i in range(7, 13):
    print('*' * (12 -i))

print('\nSquare\n')

for i in range(1, 7):
    print('*' * 6)

print('\nPyramid\n')
    
for i in range(0, 6):
    print(f"{' ' * (6 - i)}{'*' * (2 * i + 1)}")

print('\nTriangle\n')
    
for i in range(0, 6):
    print(f"{'*' * (2 * i + 1)}")


### Onomatopoeia
data = [
    # Korean Onomatopoeia
    ("개굴개굴", "gaegul-gaegul", "Ribbit (frog sound)"),
    ("멍멍", "meong-meong", "Woof (dog barking)"),
    ("야옹", "ya-ong", "Meow (cat sound)"),
    ("딸랑딸랑", "ddal-lang-ddal-lang", "Jingle (bell sound)"),
    ]


print ("\nJust words:")


justwords = []
for word in data:
    justwords.append(word[0]) 
    
print (justwords)

#OR use list comprehension

justwords = [w[0] for w in data] 

print (justwords)

print ("\nSorted:")

print (sorted(justwords))
