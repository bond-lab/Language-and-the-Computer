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
#url = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"

### and since last year!  Web data changes, ...

url = "https://www.gutenberg.org/files/48320/48320-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf-8')

#print (raw[:100])

##
## CHOP
##

# Need to find where to start and stop by looking at the file.

start=raw.index("Adventure VIII") 
stop=raw.index("Adventure IX")
story=raw[start:stop]


##
## SAVE
##

f = open("spec.txt", 'w')
f.write(story)

##
## Download 
##
import os

if os.getenv("COLAB_RELEASE_TAG"):
    from google.colab import files
    files.download('/content/spec.txt')


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
    ### add all the lines together, then split into sentences
    raw += l
sents  = len(nltk.sent_tokenize(raw))

print(f"This text of the Speckled Band has {chars:,d} characters, {lines:,d} lines, {sents:,d} sentences and {tokens:,d} tokens.")

