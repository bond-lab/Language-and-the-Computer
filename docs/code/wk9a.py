#    Working with someone else, take turns to pick a word that can be
#    either a noun or a verb (e.g. contest); the opponent has to
#    predict which one is likely to be the most frequent in the Brown
#    corpus; check the opponent's prediction, and tally the score over
#    several turns.

import nltk

### From the treebank corpus make a list of all present participles
### ('VBG'), and then collect a list of all the word-tag pairs that
### immediately precede items in that list.

tbt = nltk.corpus.brown.tagged_words()

part = [w for (w,p) in tbt if p.startswith('VBG')]
print('10 Present Particples:', part[:10])

pre_present_participle = []
for i in range(len(tbt)):
    if tbt[i][1].startswith('VBG'):
        pre_present_participle.append(tbt[i-1][1])
        ##print (tbt[i-1], tbt[i])

print(nltk.FreqDist(pre_present_participle).most_common()) 

### From the brown corpus make a list of all adverbs using the universal tag set ('ADV'), and show the tags that follow them and their frequencies.
bwts = nltk.corpus.brown.tagged_words(tagset='universal')

adverbs = [w for (w,p) in bwts if p=='ADV']
print('10 Adverbs:', adverbs[:10])

post_adverb_tags = []
for i in range(len(bwts)):
    if bwts[i][1] == 'ADV':
        post_adverb_tags.append(bwts[i+1][1])

print(nltk.FreqDist(post_adverb_tags).most_common()) 


### Create a default dictionary that gives the value 'UNKNOWN' for an unknown key. 

from collections import defaultdict as dd
pos = dd(lambda: 'UNKNOWN')

print (pos['thingamajig'])

