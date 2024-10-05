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


print("\nMin, Max and Sum of 1..1,000,000\n")
million = range(1, 1_000_001)

print(min(million))
print(max(million))
print(sum(million))

print('\nSplitting Guests\n')
guests = ['C. J. Cherryh', 'Conan Doyle', 'Marie Curie', 'Isaac Newton', 'Dorothy Sayers', 'Oscar Wilde']
list1 = guests[::2]
list2 = guests[1::2]
print(guests)
print(list1)
print(list2)

print('\nSquares\n')

for squares in [(i, i*i) for i in range (1,10)]:
    print(f"The square of {squares[0]} is {squares[1]}")

# OR 
print('\nMore Pythonic Squares\n')

for (i, s) in [(i, i*i) for i in range (1,10)]:
    print(f"The square of {i} is {s}")

# countdown in Japanese    
japanese_numerals = ("一", "二", "三", "四", "五", "六", "七", "八", "九", "十")

countdown = []
for n in reversed(japanese_numerals):
    countdown.append(n)

print(countdown)

## or
countdown = japanese_numerals[::-1]

print(countdown)

countdown = list(japanese_numerals[::-1])

print(countdown)

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
