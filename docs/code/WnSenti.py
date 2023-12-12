###
### Model Solution for HG2051 Project 1 2021
###
### by Francis Bond (2021)
### released into the public domain
###

import wn
from collections import defaultdict as dd
import numpy as np
import sys
import re
sentidata = "ntumc-senti.tsv"
wn.download('omw-en')
wn = wn.Wordnet(lexicon='omw-en:1.4')
prefix='omw-en'


def load_senti(data, threshold=0.05, debug=False):
    """
    load the sentiment data
    store it in a dictionary indexed by lemma
    discard if:
       * no lemma is found
       * |score| < threshold 
    return the dictionary
    based on the fact that we know 'omw-en' uses similar IDs as the corpus
    """
    lsentiment = {}
    ssentiment = {}
    senti = dd(list)
    for l in open(data):
        (tag, lemma, score, scores) = l.strip().split('\t')
        score = float(score) / 100
        ## try to find the synset in wordnet
        try:
            ss = wn.synset(id = f'{prefix}-{tag}')
        except:
            try:
                ss = wn.synset(id = f'{prefix}-{tag}'.replace('-a', '-s'))
            except:
                if debug:
                    print("couldn't find synset", tag)
                continue

        if abs(score) > threshold:
            senti[ss.id].append(score)
        else:
            senti[ss.id].append(0.0)
        ### try to find the lemma in wordnet
        senses = set()
        for s in ss.senses():
            #print(s)
            for f in s.word().forms():
                #print(f'{f}')
                f = f.replace('(a)', '')
                f = f.replace('(p)', '')
                if f.lower() in [lemma,
                                 lemma.lower(),
                                 lemma.lower().replace(' ','_'),
                                 lemma.lower().replace('-','_'),
                                 lemma.lower().replace('-',''),
                                 lemma.lower().replace(' ','')]:
                    #print('FOUND')
                    senses.add(s)
        #print(f'{senses=}')
        try:
            match = senses.pop()
            #print(f'LEM {len(senses)} {match} {senses}')
        except:
            if debug:
                print(f"couldn't find '{lemma}' in {ss}")
                print ([x.word().lemma() for x in ss.senses()])
            continue
        if abs(score) > threshold:
            lsentiment[match.id] = score
        else:
            lsentiment[match.id] = 0.0
        if len(senses) > 0:
            if debug:
                print(f"multi {senses}")
    for s in senti:
        #print(s, senti[s], np.mean(senti[s]))
        ssentiment[s] = np.mean(senti[s])
    ## return the average sentiment for each lemma,
    ## and for each synset
    #print('LEM len', len(lsentiment))
    return lsentiment, ssentiment




if __name__ == "__main__":
    lsnt, ssnt = load_senti(sentidata)

    ##
    ## print our the numbers of senses and sentiments with lemmas
    ##

    with open('table1.tex', 'w') as tab1:
        print(f"""
        & Synsets No. & Score & Lemmas No. & Score \\\\
        All      & {len(ssnt):,d}   
        & {np.mean([ssnt[s] for s in ssnt]):+.3f}  
        & {len(lsnt):,d}   
        & {np.mean([lsnt[s] for s in lsnt]):+.3f}  
        \\\\
        Non-Zero & {len([s for s in ssnt if ssnt[s] != 0]):,d}
        & {np.mean([ssnt[s] for s in ssnt if ssnt[s] != 0]):+.3f} 
        & {len([s for s in lsnt if lsnt[s] != 0]):,d}   
        & {np.mean([lsnt[s] for s in lsnt if lsnt[s] != 0]):+.3f}  
        \\\\
        Positive & {len([s for s in ssnt if ssnt[s] > 0]):,d}

        & {np.mean([ssnt[s] for s in ssnt if ssnt[s] > 0]):+.3f} 
        & {len([s for s in lsnt if lsnt[s] > 0]):,d} 
        & {np.mean([lsnt[s] for s in lsnt if lsnt[s] > 0]):+.3f}  
        \\\\
        Negative & {len([s for s in ssnt if ssnt[s] < 0]):,d}
        & {np.mean([ssnt[s] for s in ssnt if ssnt[s] < 0]):+.3f} 
        & {len([s for s in lsnt if lsnt[s] < 0]):,d}   
        & {np.mean([lsnt[s] for s in lsnt if lsnt[s] < 0]):+.3f}  
        """, file = tab1)



    max_l_sent = max([lsnt[s] for s in lsnt])
    min_l_sent = min([lsnt[s] for s in lsnt])
    print(f"Most positive senses ({max_l_sent}): {', '. join([wn.sense(l).word().lemma() for l in lsnt if lsnt[l]==max_l_sent])}")
    print(f"Most negative senses ({min_l_sent}): {', '. join([wn.sense(l).word().lemma() for l in lsnt if lsnt[l]==min_l_sent])}")



    ## Take a look at the data
    # for l in lsnt:
    #     if abs(lsnt[l]) > 0.05:
    #         print (l, lsnt[l])
    # for s in ssnt:
    #     if abs(ssnt[s]) > 0.05:
    #         print (s, ssnt[s])

    ###
    ### Synset relations
    ###

    def synset_diffs(ssnt, relation, nonzero=False):
         """
         find the average difference for all synsets related by the 
         'similar to' relation which have non-zero sentiment
         """
         diffs = []
         ## look at all the synsets we have sentiment for
         for s1 in ssnt:
             ss1=wn.synset(id=s1)
             for ss2 in ss1.get_related(relation):
                 s2 = ss2.id
                 #print (s1, s2)
                 ## look at all synsets similar_to them
                 ## but only in one direction
                 if s1 < ss2.id:
                     continue
                 if (s1 in ssnt) and  (s2 in ssnt):
                     if nonzero and (ssnt[s2] == 0.0  or ssnt[s1] == 0.0):
                         continue
                     diff = (abs(ssnt[s1] - ssnt[s2]))
                     diffs.append(diff)
                     #print (s1, s2, ssnt[s1], ssnt[s2],diff)
                     #print(s1.definition())
                     #print(s2.definition())
         return diffs # or np.mean(diffs)



    with open('table2.tex', 'w') as tab2:
        for relation in ['similar', 'hyponym', 'holo_location',
                         'holo_member',
                         'holo_part',
                         'holo_portion',
                         'holo_substance', 'holonym',
                         'entails', 'causes', ]:
     # 'mero_location', 'mero_member'
     #                     'mero_part', 'mero_portion', 'mero_substance', 'meronym',
     #    ]:
            withzero = synset_diffs(ssnt, relation)
            withoutzero=synset_diffs(ssnt, relation, nonzero=True)
            print(relation.replace('_', ' '), 
                  len(withzero), f"{np.mean(withzero):+.3f}", 
                  len(withoutzero), f"{np.mean(withoutzero):+.3f}", 
                  sep = ' & ', end = '\\\\\n', file=tab2)


    ###
    ### Sense relations
    ###


    def lemma_diffs(lsnt, relation, nonzero=False):
         """
         find the average difference for all synsets related by the 
         'similar to' relation which have non-zero sentiment
         """
         diffs = []
         ## look at all the synsets we have sentiment for
         if relation ==  'antonym_opposite':
             opposite = True
             relation =  'antonym'
         else:
             opposite = False
         for l1 in lsnt:
            lm1 = wn.sense(id=l1)
            for lm2 in lm1.get_related(relation):
                 l2=lm2.id  
                 #print (s1, s2)
                 ## look at all synsets similar_to them
                 ## but only in one direction
                 if l1 < l2:
                     continue
                 if (l1 in lsnt) and  (l2 in lsnt):
                     if nonzero and (lsnt[l2] == 0.0  or lsnt[l1] == 0.0):
                         continue
                     if opposite:
                         diff = (abs(lsnt[l1] + lsnt[l2]))
                     else:
                         diff = (abs(lsnt[l1] - lsnt[l2]))
                     diffs.append(diff)
                     #print (relation, l1, l2, lsnt[l1], lsnt[l2], diff, opposite)
                     #print(s1.definition())
                     #print(s2.definition())
         return diffs # or np.mean(diffs)

    with open('table3.tex', 'w') as tab2:
        for relation in ['antonym',
                         'antonym_opposite',
                         'derivation',
                         'also',
                         'pertainym',  ]:
     # 'mero_location', 'mero_member'
     #                     'mero_part', 'mero_portion', 'mero_substance', 'meronym',
     #    ]:
            withzero = lemma_diffs(lsnt, relation)
            withoutzero=lemma_diffs(lsnt, relation, nonzero=True)
            print(relation.replace('_', ' '), 
                  len(withzero), f"{np.mean(withzero):+.3f}", 
                  len(withoutzero), f"{np.mean(withoutzero):+.3f}", 
                  sep = ' & ', end = '\\\\\n', file=tab2)

