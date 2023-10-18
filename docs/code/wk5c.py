# -*- encoding: utf-8 -*-


# Load wordnet inside python using the wn module

import wn

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
    
