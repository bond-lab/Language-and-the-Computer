##
## Write a program to: 
## (i) get the text of the Speckled Band (Sherlock Holmes)
##  * go to gutenberg and search for 'Speckled Band'
##  * find the url of the textfile
##  * read it in
## (ii) save it as a file called "spec.txt"
## (iii) read it in and count lines, words, tokens
##
from urllib import request
import nltk 
## Read

### Note URL has changed since the book was published
url = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"
response = request.urlopen(url)
raw = response.read().decode('utf-8')
#print (raw[:100])

##
## CHOP
##
start=raw.index("THE ADVENTURE OF THE SPECKLED BAND") 
stop=raw.index("THE ADVENTURE OF THE ENGINEER'S THUMB")
story=raw[start:stop]
##
## SAVE
##

f = open("spec.txt", 'w')
f.write(story)

###
### read
###
f = open("spec.txt", 'r')
chars=0
lines=0
tokens=0
raw = ''
for l in f:
    lines  += 1
    chars  += len(l)
    tokens += len(nltk.word_tokenize(l.strip()))
    ### just for fun
    raw += l.strip() + ' '
sents  = len(nltk.sent_tokenize(raw))

print("This text of the Speckled Band has {:,d} characters, {:,d} lines, {:,d} sentences and {:,d} tokens.".format(chars, lines, sents, tokens))
