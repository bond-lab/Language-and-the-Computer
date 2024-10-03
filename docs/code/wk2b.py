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

onomatopoeia_data = [
    # Korean Onomatopoeia
    [
        ("개굴개굴", "gaegul-gaegul", "Ribbit (frog sound)"),
        ("멍멍", "meong-meong", "Woof (dog barking)"),
        ("야옹", "ya-ong", "Meow (cat sound)"),
        ("딸랑딸랑", "ddal-lang-ddal-lang", "Jingle (bell sound)"),
    ],
    
    # Chinese Onomatopoeia
    [
        ("汪汪", "wāng wāng", "Woof (dog barking)"),
        ("喵喵", "miāo miāo", "Meow (cat sound)"),
        ("哗啦啦", "huā lā lā", "Splash (water flowing)"),
    ],
    
    # Vietnamese Onomatopoeia
    [
        ("meo meo", "", "Meow (cat sound)"),
        ("gâu gâu", "", "Woof (dog barking)"),
        ("ục ịch", "", "Splash (water or something heavy dropping in water)"),
        ("ro ro", "", "Purr (cat sound)"),
    ],
    
    # Indonesian Onomatopoeia
    [
        ("guk guk", "", "Woof (dog barking)"),
        ("meong", "", "Meow (cat sound)"),
        ("kring kring", "", "Ring (phone or bell sound)"),
    ],
    # Japanese Onomatopoeia
    [
        ("ワンワン", "wan wan", "Woof (dog barking)"),
        ("ニャーニャー", "nyaa nyaa", "Meow (cat sound)"),
        ("ピヨピヨ", "piyo piyo", "Tweet (bird chirping)"),
        ("ゴロゴロ", "goro goro", "Purring (cat purr) / Rolling"),
    ]
    ]

print ("\nJust Korean:")
# we know Korean is the first list
print (onomatopoeia_data[0])

print ("\nJust words:")


justwords = []
for lang in onomatopoeia_data:
    newlang = []
    for word in lang:
        newlang.append(word[0])
    justwords.append(sorted(newlang)) 

    
print (justwords)

#OR use list comprehension

justwords = []
for lang in onomatopoeia_data:
    justwords.append(sorted([w[0] for w in lang])) 

print (justwords)
