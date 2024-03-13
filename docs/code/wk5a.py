import nltk 
#
# 1: Find the 50 most frequent words in emma
#

print("Find the 50 most frequent words in emma")

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
## or 
print(nltk.FreqDist(emma).most_common(50))
## or
print([t[0] for t in nltk.FreqDist(emma).most_common(50)])
print()


print("Find the 50 most frequent words in emma without stopwords")
from nltk.corpus import stopwords
stopen = stopwords.words('english')

print(nltk.FreqDist(w for w in emma if w not in stopen).most_common(50))
print()

### faster: just look at the high frequency words (assume that 500 words is enough) 
### faster: just look at the high frequency words (assume that 500 words is enough)
print("Find these faster by only looking at the most frequent words")
print([t[0] for t in nltk.FreqDist(emma).most_common(500)
       if t[0] not in stopen][0:50])
print()

# A Pronouncing Dictionary
# Most words in the dictionary have the same first phonetic code as their first letter:
# E.g.: for ('fir', ['F', 'ER1']) 'f' is the same as 'F'
# Sometimes they do not
# E.g.: for ('yves', ['IY1', 'V'])
# What proportion of the words start with the same code?
# What are some common mismatches? 

  	

cmu  = nltk.corpus.cmudict.entries()

print("%f of the words start with the same code" % \
(1.0 * len([w for (w, l) in cmu if w[0] == l[0].lower()]) / len(cmu)))

## find irregular paterns
## Easy print them all and eyball them
for (w, l) in cmu:
    if  w[0] != l[0].lower():
        print(w, l)

## Could  count them
#print([(w[0], l[0]) for (w, l) in cmu if w[0] != l[0].lower()][:10]
print(nltk.FreqDist([(w[0], l[0]) for (w, l) in cmu if w[0] != l[0].lower()]).most_common(20))

###
### I like the new wn module
###
### you may have to install it
### pip install wn
###
print("\n\nLook up wordnet using the wn module\n\n")


import wn

wn.download('omw-en:1.4')
wnen = wn.Wordnet('omw-en:1.4')

def show(ss):
    print (ss.id, ss.lemmas())

print("Synset for student and its hypnonyms")
for ss in wnen.synsets('student'):
    show(ss)
    print("Hyponyms: ")
    for s in ss.hyponyms():
        show(s)
    print()
    print()

print("Synset for student and its hypernyms")
for ss in wnen.synsets('student'):
    show(ss)
    print("Hypernyms: ")
    for s in ss.hypernyms():
        show(s)
    print()
    print()
    
print("Synset for professor its hypernyms")
for ss in wnen.synsets('professor'):
    show(ss)
    print("Hypernyms: ")
    for s in ss.hypernyms():
        show(s)
    print()
    print()

print("Some size adjectives and their antonyms")

for a in ['big', 'large', 'great']:
    for ss in wnen.synsets(a):
        show(ss)
        for s in ss.senses():
            print(s.id, s.word().forms())
            for a in s.get_related('antonym'):
                print ('<=> ', a.id, a.word().forms())
        print()
    print()

for a in "big/large/great".split('/'): 
    for n in "sister/uncle/toe".split('/'):
        w = f"{a} {n}"
        if wnen.synsets(w):
            print(w)
            for s in wnen.synsets(w):
                show(s)
















###
### Or you can use nltk
###

print("\n\nLook up wordnet using nltk\n\n")

from nltk.corpus import wordnet as wn

for ss in wn.synsets('student'):
    print(ss)
    print("Hyponyms: ")
    for s in ss.hyponyms():
        print(s, )
    print()
    print()

for ss in wn.synsets('student'):
    print(ss)
    print("Hypernyms: ")
    for s in ss.hypernyms():
        print(s, )
    print()
    print()

for ss in wn.synsets('professor'):
    print(ss)
    print("Hypernyms: ")
    for s in ss.hypernyms():
        print(s, )
    print()
    print()

for a in ['big', 'large', 'great']:
    for ss in wn.synsets(a):
        print(ss)
        for l in ss.lemmas():
            print(l, l.antonyms())
        print()
    print()

for a in "big/large/great".split('/'): 
    for n in "sister/uncle/toe".split('/'):
        w = "%s_%s" % (a, n)  ## wordnet uses '_' as word separator
        # print(w
        if wn.synsets(w):
            print(w, wn.synsets(w))
