# -*- encoding: utf-8 -*-

import nltk 
from nltk.corpus import stopwords

###  Find the 50 most frequent bigrams (see Week 6) in Jane Austen's Emma.
###  Then find the 50 most frequent bigrams that do not include a stopword.
emma = nltk.corpus.gutenberg.words('austen-emma.txt')

print ("Find the 50 most frequent bigrams in emma")
print ([b[0] for b in nltk.FreqDist(nltk.bigrams(emma)).most_common(50)])

print ("Find the 50 most frequent bigrams in emma without stopwords")

stopen = stopwords.words('english')

# that do not contain stopwords (or punct)

print (nltk.FreqDist(nltk.bigrams(w for w in emma 
                                 if w not in stopen 
                                 and w.isalpha())).most_common(50))

### find the bigrams first then remove stop words
print ("Find the 50 most frequent bigrams without stopwords in emma")
print (nltk.FreqDist((w1, w2) for (w1, w2) in nltk.bigrams(w for w in emma
                                                          if w.isalpha())
                     if w1 not in stopen and w2  not in stopen).most_common(50))



###
### A Pronouncing Dictionary
###


pron = nltk.corpus.cmudict.entries()

print("First ten entries", pron[:10])

# Find python in the Pronouncing Dictionary and print its pronunciation.
python_pron = [p for w,p in pron if w =='python']
print("Python is pronounced", python_pron)

# Find marathon and print its pronunciation.
marathon_pron = [p for w,p in pron if w =='marathon']
print("Marathon is pronounced", marathon_pron)


# Find all the words whose last syllable rhymes with python.
# Find all the words whose last syllable rhymes with marathon. 

for word in ['python', 'marathon']:
    wp = [p for w,p in pron if w ==word]
    print("{} is pronounced {}".format(word, wp))
    print("These words rhyme with it (assuming last three phonemes are ok):")
    print([(w,p[-3:]) for w,p in pron if len(p)>2 and wp[0][-3:]==p[-3:]])

## A better definition of "rhyme" is 
### "identical in pronunciation from the main-stressed vowel to the end",
### See: http://languagelog.ldc.upenn.edu/nll/?p=1946


### And of course: http://en.wiktionary.org/wiki/Rhymes:English

# ★ Write a function that converts Arbabet to IPA
# Use it to print the pronunciations of python and marathon

# Load wordnet inside python.

from nltk.corpus import wordnet as wn

print ("\nWordnet\n")

#     Look at the different synsets for bird.

print ("Synsets for bird:")
print (wn.synsets('bird'))

#     How many are there?

print ("# of senses for bird:", len(wn.synsets('bird')))

#     How deep in the hierarchy and what are the definitions?

for s in wn.synsets('bird'):
    print (s.name(), s.min_depth(), s.definition())


print("\nWhich  languages have lemmas for 'bird.n.01'?")
for l in wn.langs():
    ### bug in Croation and Bulgarian, my bad
    # if l in ('hrv', 'bul'):
    #     continue ## skip to the next language
    if wn.synset('bird.n.01').lemmas(lang=l):
        print (l, end=': ')
        print(",".join(wn.synset('bird.n.01').lemma_names(lang=l)))


#     For each synset, print out each lemma and its frequency (hint freqency of a lemma is given by lemma.count)

for s in wn.synsets('bird'):
    print(s)
    for l in s.lemmas():
        print (l.name(), l.count())
    print()
    
#     Give the total frequency for each synset 

for s in wn.synsets('bird'):
    print (s.name(), sum(l.count() for l in s.lemmas()), s.definition())
    

# ★ Tabulate the average polysemy per word length for all words in wordnet, and then seperately for each part of speech. (Hint: polysemy is number of synsets/word; you can get all words by [w for w in wn.all_lemma_names()]; for just nouns you can do: [w for w in wn.all_lemma_names('n')]. ) 


##
## another way to do it
##

cmu = nltk.corpus.cmudict.dict()

# Find python in the Pronouncing Dictionary and print its pronunciation.

print ("'python' is pronounced:", cmu['python'])

    # Find marathon and print its pronunciation.

print ("'marathon' is pronounced:", cmu['marathon'])
##
## simple
##

## A better definition of "rhyme" is 
### "identical in pronunciation from the main-stressed vowel to the end",
### See: http://languagelog.ldc.upenn.edu/nll/?p=1946

##
## complicated but fully automatic
##

for pos in ['all', 'n', 'v', 'a', 'r']:
    poly = nltk.defaultdict(list)
    print ("\nWordlength: Average Polysemy for %s:" % pos)
    if pos == 'all':
        for w in wn.all_lemma_names():
            poly[len(w)].append(len(wn.synsets(w)))
    else:
        for w in wn.all_lemma_names(pos):
            poly[len(w)].append(len(wn.synsets(w)))
    for length in sorted(poly.keys()):
        print ("%2d: %2.2f" % (length, 1.0 * sum(poly[length]) / 
                              len(poly[length])))





def lastsyllable (pron):
    "take the pronunciation from cmudict, return the last syllable"
    # e.g. ['P', 'AY1', 'TH', 'AA0', 'N'] -> ['TH', 'AA0', 'N']
    end = []
    nrop = pron[::-1]
    if len(pron) ==1:
        ## 'I'
        return pron
    for l in nrop:
        end.insert(0,l)
        ## stop when we come to a vowel
        if l[-1].isdigit() and nrop.index(l) != 0:
            ## add the precceding phoneme as well if there is one
            ## don't do this if it is the second vowel 'Hammer'
            if len(end) < len(nrop) and \
                len([c for c in end if c[-1].isdigit()]) < 2:  
                end.insert(0,nrop[len(end)])
            return end

def rhymes(word, pdict):
    for pron in pdict[word]:
        print ("Rhymes for:", word, pron, lastsyllable(pron))
        end = lastsyllable(pron)
        for w, prons in pdict.items():
            for p in prons:
                if p[-len(end):] == end and w != word:
                    print (w, p)
        print()

 
rhymes('python', cmu)
rhymes('orange', cmu)
rhymes('love', cmu)

rhymes('hammer', cmu)
rhymes('accident', cmu)

rhymes('eye', cmu)
