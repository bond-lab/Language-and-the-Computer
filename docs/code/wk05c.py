print("\n\nCount Vowels\n")

def count_vowels(word):
    """
    count the number of vowels in a word
    """
    vowels='aeiou'
    count = 0
    for c in word:
        if c in vowels:
            count +=1
    return count


print("hello", count_vowels("hello"))  # Expected output: 2

print("Python", count_vowels("Python")) # Expected output: 1


print("\n\nCount Czech Vowels\n")

def count_any_letters(word, letters='aeiou'):
    """
    count the number of letters in a word
    you can give the letters as a second argument
    """
    count = 0
    for c in word.lower():
        if c in letters:
            count +=1
    return count

def count_vowels(word):
    """
    For Czech!
    """
    return count_any_letters(word, letters='aeiouyáéíýóúů')

print("Válka", count_vowels("Válka"))  # Expected output: 2
print("Krk", count_vowels("Krk")) # Expected output: 0
print("Ano", count_vowels("Ano")) # Expected output: 2

print("\n\nRepeated words\n")

def repeats(words):
    """
    take a list of words and warn if there are any words that appear twice in a row
    """
    for i in range(len(words) - 1):
        # if a word is the same as the next word
        if words[i].lower() == words[i+1].lower():
            print(f"'{words[i].lower()}' repeated in position {i}")

print(['The', 'the', 'book', 'is', 'very', 'very', 'good'])  
repeats(['The', 'the', 'book', 'is', 'very', 'very', 'good'])
# expect 'The repeated in position 0', 'very repeated in position 4'

repeats(["hello", "world", "hello"])
print(["hello", "world", "hello"])


print("Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo")
print("(Buffalonian bison whom other Buffalonian bison bully also bully Buffalonian bison.)")
repeats("Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo".split())




print("\n\nUpdate Inventory\n")

def update_inventory(inventory, *new_items):
    """
    Updates the inventory with new items.

    Returns:
    dict: The updated inventory with the new items and their counts.
    """
    for item in new_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

# Example dictionary and function call
current_inventory = {"apple": 2, "banana": 3}
new_inventory = update_inventory(current_inventory, "apple", "banana", "cherry")
print(new_inventory)
