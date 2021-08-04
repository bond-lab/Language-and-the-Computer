###
### Write regular expressions to match the following classes of strings:
###    1. A single determiner (assume that a, an, and the are the only determiners).
###    2. An arithmetic expression using integers, addition, and multiplication, 
###       such as 2*3+8.
###

import nltk
import re
from urllib import request
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
    '''Get cleaned text from a URL'''
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

print (request.urlopen('http://www3.ntu.edu.sg/home/fcbond/').read().decode('utf-8')[:40])
print (gettextfromurl('http://www3.ntu.edu.sg/home/fcbond/')[:40])

###
### Create a function plural() that takes a word and returns its plural form.
### Test it on dog, apple, fly, boy, woman. 
###

irregular={'chess':'chess'}
## from the ERG http://svn.delph-in.net/erg/trunk/irregs.tab
irregs = request.urlopen('http://svn.delph-in.net/erg/trunk/irregs.tab').read().decode('utf-8')

for l in irregs.splitlines():
    things = l.strip().split()
    if len(things) == 3 and things[1] == 'N_PL_OLR':
        irregular[things[2]]=things[0]

### or make a local copy
#fh = open('irregs.tab')
#for l in fh:
# same as above
        
def plural(w):
    """return the plural of a word"""
    if word in irregular:
        plural = irregular[word]
    # if (re.search(r'^(man|woman|policeman|fireman)$', w)):
    #     return re.sub(r'man$', 'men', w)
    elif (re.search(r'[^aeiou]y$', w)):
        return re.sub(r'y$', 'ies', w)
    elif re.search(r'ch|sh|s|z|x', word):
        plural = word+'es'
    else:
        return w +'s'

for word in "dog, apple, fly, boy, woman, chess, ox, stomach, octopus".split(", "):
    print (word, plural(word))

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
from nltk.corpus import wordnet as wn

endprep = re.compile(r"^(\w+)_(abaft|aboard|about|above|absent|across|afore|after|against|along|alongside|amid|amidst|among|amongst|an|anenst|apropos|apud|around|as|aside|astride|at|athwart|atop|barring|before|behind|below|beneath|beside|besides|between|beyond|but|by|circa|concerning|despite|down|during|except|excluding|failing|following|for|forenenst|from|given|in|including|inside|into|lest|like|mid|midst|minus|modulo|near|next|notwithstanding|of|off|on|onto|opposite|out|outside|over|pace|past|per|plus|pro|qua|regarding|round|sans|save|since|than|through,|throughout|till|times|to|toward|towards|under|underneath|unlike|until|unto|up|upon|versus|via|vice|with|within|without|worth)$")

def inflectv(verb):
    '''very simple: should use the irregulars from above'''
    return [v, v+'ing', v+'en', v+'ed', v+'s']

allverbs=list(wn.all_synsets('v'))
for s in allverbs[:20]:
    for l in s.lemma_names():
        m = re.search(endprep,l)
        if m:
            (v,p) = m.groups()
            for vv in inflectv(v):
                print (vv,p)

###
### FIXME: store and  match against texts, improve the inflection
###
