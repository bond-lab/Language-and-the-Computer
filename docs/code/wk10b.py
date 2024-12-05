# -*- encoding: utf-8 -*-

from collections import defaultdict as dd
from numpy import mean

# Load wordnet inside python using the wn module

import wn
### make sure I don't load any other wordnets
wn.config.data_directory = 'wn_data' 

wn.download('omw:1.4')

ewn = wn.Wordnet('omw-en:1.4')


print ("\nWordnet\n")

#     Look at the different synsets for bird.

print ("Synsets for bird:")
print (ewn.synsets('bird'))

#     How many are there?

print ("# of senses for bird:", len(ewn.synsets('bird')))

#     How deep in the hierarchy and what are the definitions?

for s in ewn.synsets('bird'):
    print (s.id, s.min_depth(), s.definition())


print("\nWhich  languages have lemmas for 'omw-en-01503061-n'?")
for l in set([l.language for l in wn.lexicons()]):
    for t in ewn.synset(id='omw-en-01503061-n').translate(lang=l):
        print (l, t, t.lemmas())


#     For each synset, print out each sense and its frequency (hint freqency of a sense is given by sense.counts(), which returns a list of numbers )

for ss in ewn.synsets('bird'):
    print(ss)
    for s in ss.senses():
        print (s.id, sum(s.counts()))
    print()
    
#     Give the total frequency for each synset 

for ss in ewn.synsets('bird'):
    print (ss.id, sum(sum(s.counts()) for s in ss.senses()), ss.definition())


##
## find all the hyponyms of the color red! (hint use closure)
##
print("\n\nSysnets for 'red'\n\n")

# which is the color?
for ss in ewn.synsets('red'):
    print(ss.id, ss.lemmas(), ss.definition())

print("\n\nAll Hyponyms of 'red'\n\n")

for ss in  ewn.synsets('red')[4].closure('hyponym'):
    print(ss.id, ss.lemmas(), ss.definition())

###
### Polysemy by length
###
stats= dict()

stats['n'] = dd(list)
stats['v'] = dd(list)
stats['a'] = dd(list)
stats['r'] = dd(list)
stats['ALL'] = dd(list)



for w in ewn.words():
    length = len(w.lemma())
    polysemy = len(w.synsets())
    pos = w.pos
    stats['ALL'][length].append(polysemy)
    stats[pos][length].append(polysemy)


print('\n\nAverage Polysemy vs Word Length (English)\n\n')
    
for pos in stats:
    print(f'\nPOS = {pos}')
    for l in sorted(stats[pos]):
        print(l, mean(stats[pos][l]), sep = '\t')
    
