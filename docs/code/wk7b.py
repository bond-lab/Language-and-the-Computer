###
### Write regular expressions to match the following classes of strings:
###    1. A single determiner (assume that a, an, and the are the only determiners).
###    2. An arithmetic expression using integers, addition, and multiplication, 
###       such as 2*3+8.
###

import nltk
import re
from urllib import request
from nltk.book import text1, text2, text3, text4, text5, text6, text7, text8, text9
### Articles

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
[w for w in wordlist if re.search(r'^(an?|the)$', w)]
['a', 'an', 'the']

# Or just matching on text

## '\b([Aa][Nn]?|[Tt][Hh][Ee])\b'


### Arithmetic

nltk.re_show(r'8', ' I can\'t do 2*8+4 in my head')
# I can't do 2*{8}+4 in my head
nltk.re_show(r'[\d+*]+', ' I can\'t do 2*8+4 in my head')
# I can't do {2*8+4} in my head
nltk.re_show(r'[\d+*-/]+', ' I can\'t do 2*8+4 in my head')
# I can't do {2*8+4} in my head

# raw_contents = urllib.urlopen('http://www.nltk.org/').read()

# print (raw_contents)

###
### Write a utility function that takes a URL as its argument, and
### returns the contents of the URL, with all HTML markup removed. Use
### urllib.urlopen to access the contents of the URL,
### e.g. raw_contents = urllib.urlopen('http://www.nltk.org/').read().
###
def gettextfromurl(url):
    """Get cleaned text from a URL"""
    ## get the raw html
    cooked = request.urlopen(url).read().decode('utf-8');
    ## lose the line endings
    cooked = re.sub(r'\n', ' ', cooked)
    # ## lose the javascript
    cooked = re.sub(r'<script.*?script>', '', cooked, re.S)
    ## lose the html tags
    cooked = re.sub(r'<.*?>', '', cooked)
    ## clean up whitespace
    cooked = re.sub(r'\s+', ' ', cooked)
    return cooked

print (request.urlopen('https://fcbond.github.io/').read().decode('utf-8')[:40])
print (gettextfromurl('https://fcbond.github.io/')[:40])

###
### Create a function plural() that takes a word and returns its plural form.
### Test it on dog, apple, fly, boy, woman. 
###

irregular={'chess':'chess'}
## from the ERG http://svn.delph-in.net/erg/trunk/irregs.tab
irregs = request.urlopen('http://svn.delph-in.net/erg/trunk/irregs.tab').read().decode('utf-8')

for l in irregs.splitlines():
    things = l.strip().split()
    if len(things) == 3 and things[1] in ('N_PL-IRREG_OLR',
                                          'N_PL-IRREG-NOAFF_OLR'):
        irregular[things[2]]=things[0]

### or make a local copy
#fh = open('irregs.tab')
#for l in fh:
# same as above
        
def plural(w):
    """return the plural of a word"""
    if word in irregular:
        plural = irregular[word]
    elif (re.search(r'[^aeiou]y$', w)):
         plural = re.sub(r'y$', 'ies', w)
    elif re.search(r'ch|sh|s|z|x', word):
        plural = word+'es'
    else:
        plural = w +'s'
    return plural

for word in "dog, apple, fly, boy, woman, chess, ox, stomach, octopus".split(", "):
    print (word, plural(word))


###
### Save some text into a file corpus.txt.
### Define a function load(f) that reads
### from the file named in its sole argument,
### and returns a string containing the text of the file.
###

fh = open('corpus.txt', 'w')
fh.write(gettextfromurl('https://fcbond.github.io/'))
fh.close()

def load(f):
    """
    read a file into a string
    """
    fh = open(f)
    text = fh.read()
    fh.close()
    return text

corpus = load('corpus.txt')

print()
print(f"loaded file {corpus[:50]}")
print()

###
### loop == list comprehension
###
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = []
for word in sent:
    word_len = (word, len(word))
    result.append(word_len)
print (result)

print ([(w, len(w)) for w in sent])

###
###
###
import wn
wn.download('omw-en')
ewn = wn.Wordnet(lexicon='omw-en:1.4')


endprep = re.compile(r"^(\w+) (abaft|aboard|about|above|absent|across|afore|after|against|along|alongside|amid|amidst|among|amongst|an|anenst|apropos|apud|around|as|aside|astride|at|athwart|atop|barring|before|behind|below|beneath|beside|besides|between|beyond|but|by|circa|concerning|despite|down|during|except|excluding|failing|following|for|forenenst|from|given|in|including|inside|into|lest|like|mid|midst|minus|modulo|near|next|notwithstanding|of|off|on|onto|opposite|out|outside|over|pace|past|per|plus|pro|qua|regarding|round|sans|save|since|than|through,|throughout|till|times|to|toward|towards|under|underneath|unlike|until|unto|up|upon|versus|via|vice|with|within|without|worth)$")

def inflectv(verb):
    '''very simple: should use the irregulars from above'''
    return [v, v+'ing', v+'en', v+'ed', v+'s']

allverbs=list(ewn.synsets(pos='v'))
vp_inflected = set()
for s in allverbs:
    for l in s.lemmas():
        m = re.search(endprep,l)
        if m:
            (v,p) = m.groups()
            for vv in inflectv(v):
                vp_inflected.add((vv,p))

print(list(vp_inflected)[:20])             
###
### FIXME: store and  match against texts, improve the inflection
###


def find_vps_in_text(text, vps):
    """
    Find all sentences with VP in
    """
    print(f"Processing {text}")
    ### get sentences, check the first 100
    raw = ' '.join(text.tokens)
    for sent in nltk.sent_tokenize(raw)[:100]:
        for (v,p) in vps:
            ### skip up to three words
            ### this both over and under matches a little, ...
            matches = re.findall(rf'(\b{v}\b\s(\b\w+\b\s){{,3}}\b{p}\b)', sent)
            if matches:
                print (f"{v} {p}", sent, sep='\n')
                print (matches)
        
find_vps_in_text(text1, vp_inflected)

#### Note that I built up the regexp bit by bit

#### verb + space + particle
#### f"{v} {p}"

#### verb + whitespace + particle, care about boundaries
#### need 'r' to show it is a raw string
#### rf"\b{v}\b\s\b{p}\b"

#### allow 0 or word in between
#### rf"\b{v}\b\s(\b\w+\b\s)?\b{p}\b"

#### allow 0 - 3 words in between
#### rf"\b{v}\b\s(\b\w+\b\s){,3}\b{p}\b"

#### match everything so it shows better
#### need {{ }} to escape { and }
#### rf"(\b{v}\b\s(\b\w+\b\s){{,3}}\b{p}\b)"
