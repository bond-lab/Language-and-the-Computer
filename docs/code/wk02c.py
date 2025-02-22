
print("\nMin, Max and Sum of 1..1,000,000\n")
million = range(1, 1_000_000 + 1)

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

