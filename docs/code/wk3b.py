person = ('Fred', 12)
(name, age) = person
if age < 2:
    print(f"{name} is a baby. Sleep Well!")
elif age < 4:
    print(f"{name} is a toddler. Be Cute!")
elif age < 8:
    print(f"{name} is an infant. Enjoy Life!")
elif age < 13:
    print(f"{name} is a child.  Learn Stuff!")
elif age < 20:
    print(f"{name} is a teenager. Have Fun!")
else:
    print(f"{name} is an adult. Work Hard!")


print("\nPlaying with guests")
guests = [('C. J. Cherryh', 31),
          ('Conan Doyle', 45),
          ('Marie Curie', 50),
          ('Isaac Newton', 21),
          ('Dorothy Sayers', 33),
          ('Oscar Wilde', 28) ]

ages = [g[1] for g in guests]

print(ages)
print(f'Average age = {sum(ages)/len(ages)}')
avg =  sum(ages)/len(ages)

print (f'Younger guests: {[g for g in guests if g[1] <= avg]}')
print (f'Older guests: {[g for g in guests if g[1] > avg]}')
print (f'Youngest guest(s): {[g[0] for g in guests if g[1] == min(ages)]}')
print (f'Oldest guest(s): {[g[0] for g in guests if g[1] == max(ages)]}')

print("\nCzech morphology 😱")

čislo = ["jeden", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset"]

for n in čislo:
    if  n == "jeden":
        teen= "jedenáct"
    elif n ==  "čtyři":
        teen =  "čtrnáct"
    elif n == 'pět':
        teen = 'patnáct'
    elif n == 'devět':
        teen =   "devatenáct"   
    elif n == 'deset':
        teen =  "dvacet" # not really a teen anymore
    else:
        teen = n + 'náct'
    print(f"{n} - {teen}") 


print("\nOnomatopoeia")

data = [
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

print("\nJust Korean")

print(data[0])

print("\nJust Latin+")

onew = []

for lang in data:
    newl = []
    for w in lang:
        if w[1]:
            newl.append(w[1])
        else:
            newl.append(w[0])
    onew.append(newl)

print(onew)
