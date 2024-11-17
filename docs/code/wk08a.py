import re

print ("\nRegular Expressions\n")

print ("[a-zA-Z]+")
print ("matches one or more ascii letters")
print ("[A-Z][a-z]*")
print ("matches zero or more ascii letters")
print ("\bp[aeiou]{,2}t\b")
print ("matches a word consisting of p followed by up to 2 vowels, followed by t")
print ("\\d+(\\.\\d+)?")
print ("matches a digit followed possibly by a full stop and more digits")
print ("([^aeiou][aeiou][^aeiou])*")
print ("Matches zero or more CVC combinations")
print ("\\w+|[^\\w\\s]+")




def extract_dates(text):
    """
    Extracts all dates in the format dd/mm/yyyy from the given text.

    >>> extract_dates("My birthday is on 25/12/1990 and my friend's is on 01/01/2000.")
    ['25/12/1990', '01/01/2000']
    >>> extract_dates("No dates here.")
    []
    """
    return re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)

print('\nExtract Dates\n')
print('Input: "My birthday is on 25/12/1990 and my friend\'s is on 01/01/2000."')
print('Output:',
      extract_dates("My birthday is on 25/12/1990 and my friend's is on 01/01/2000."))



def normalize_spaces(text):
    """
    Replaces multiple spaces between words with a single space.
    
    >>> normalize_spaces("This   is   an example    sentence.")
    'This is an example sentence.'
    >>> normalize_spaces("  Hello   world!  ")
    'Hello world!'
    """
    return re.sub(r'\s+', ' ', text).strip()

print('\nNormalize Spaces\n')
print('Input: "This   is   an example    sentence."')
print('Output:', normalize_spaces("This   is   an example    sentence."))

print('\nMask Digits\n')
print('Input:',  """My phone number is 123-456-7890.
Year: 2023
About four o'clock.
""")
print('Output:', normalize_spaces( """My phone number is 123-456-7890.
Year: 2023
About four o'clock.
"""))

def mask_digits(text):
    """
    Replaces every digit in the input text with the '#' symbol.

    >>> mask_digits("My phone number is 123-456-7890.")
    'My phone number is ###-###-####.'
    >>> mask_digits("Year: 2023")
    'Year: ####'
    >>> mask_digits("No digits here.")
    'No digits here.'
    """
    return re.sub(r'\d', '#', text)


print('\nMask Digits\n')
print('Input: "My birthday is on 25/12/1990 and my friend\'s is on 01/01/2000."')
print('Output:',
      mask_digits("My birthday is on 25/12/1990 and my friend's is on 01/01/2000."))




def count_word_occurrences(text, word):
    """
    Counts the number of times the given word appears as a standalone word in the text.
    Matching should be case-insensitive.
    
    >>> count_word_occurrences("This is an example. This is fun!", "this")
    2
    >>> count_word_occurrences("apple pie and pineapple", "apple")
    1
    >>> count_word_occurrences("Nothing to see here.", "banana")
    0
    >>> count_word_occurrences("Cat, caterpillar, and the cat.", "cat")
    2
    """
    pattern = r'\b' + re.escape(word) + r'\b'
    return len(re.findall(pattern, text, flags=re.IGNORECASE))

print('\nCount Word Occurences\n')
print('Input: "Pen, pineapple, apple-pen and pineapple-pen", "apple"')
print('Output:',
      count_word_occurrences("Pen, pineapple, apple-pen and pineapple-pen",
                             'apple'))

lyrics = """
I have a pen
I have an apple
Ah
Apple pen
I have a pen
I have pineapple
Ah
Pineapple pen
Apple pen
Pineapple pen
Ah
Pen Pie Pineapple Apple Pen
Pen Pie Pineapple Apple Pen
"""

print('Input: PPAP, "apple"')


print('Output:',
      count_word_occurrences(lyrics,
                             'apple'))

print("In:\n", lyrics)




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # normally use default verbose=False
