
# Prompt the user to enter a series of foods until they enter 'quit'
while True:
    food = input("Enter a food to cook for the party (or type 'quit' to stop): ")
    if food.lower() == 'quit':
        break
    print(f"I'll cook {food} for the party!")
print()


