###
### setup
###
import nltk
from nltk.book import *

###
###     Try out this program:
###
for i in range(1,12):
    if i <= 6:
        print('*' * i)
    else:
        print('*' * (12 -i))
##
## Try to make a different shape.
## How about a diamond?
##
for i in range(1,24,2):
    stars = ''
    if i <= 12:
        stars = '*' * i
    else:
        stars = '*' * (24 -i)
    print(stars.center(12))
###
### Write a function that prints the second letter of every word, 
### if and only if it has more than two letters. Test it on sent1
###
def second (word):
    """Print the second letter of a word, 
       if and only if it has more than two letters"""
    if len(word) > 1:
        print (word[1])

for w in sent1:
    print (w)
    second(w)
    print()

# 
# Write a program that prints out all (types of) words that appear in a text
# as both lowercase and non-lowercase in text6.
# Hint (break it down):
#     Find all unique words
#     Make two sets: one of all lowercase words and one of all non-lowercase words
#     Compare them 
print("\nMixed and lower case words (i)\n")

vocab = set(text6)
vlc = [w for w in vocab if w.islower()]
vnlc = [w for w in vocab if not w.islower()]
for w in vnlc:
    if w.lower() in vlc:
        print(w, end=' ')
### print a newline at the end
print()

print("\nMixed and lower case words (ii)\n")
### If you want it shorter
vocab = set(text6)
vlc = [w for w in vocab if w.islower()]
print(' '.join(w for w in vocab if not w.islower() and w.lower() in vlc))
