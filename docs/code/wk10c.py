# -*- encoding: utf-8 -*-

from collections import defaultdict as dd
from numpy import mean

# Load wordnet inside python using the wn module

import wn
### make sure I don't load any other wordnets
wn.config.data_directory = 'wn_data' 

wn.download('omw:1.4')

ewn = wn.Wordnet('omw-en:1.4')
jwn = wn.Wordnet('omw-ja:1.4')

for w in ewn.words(pos='n'):
    ss = w.synsets()
    ### not very efficient
    for s1 in ss:
        for s2 in ss:
            if s1.lexfile() == 'noun.animal' and s2.lexfile() == 'noun.food':
                print(w.lemma(), s1, s2)
    
for w in jwn.words(pos='n'):
    ss = w.synsets()
    ### not very efficient
    for s1 in ss:
        t1 =  s1.translate(lang='en')
        if t1 and t1[0].lexfile() == 'noun.animal':
            for s2 in ss:
                t2 = s2.translate(lang='en')
                if t2 and t2[0].lexfile() == 'noun.food':
                    print(w.lemma(), s1, s2)
    
