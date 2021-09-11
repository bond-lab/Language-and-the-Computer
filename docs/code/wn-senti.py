import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict as dd
import numpy as np
import sys
sentidata = "ntumc-senti.tsv"
###
### Sample code for HG2051 Project 1 2021
### by Francis Bond (2021)
### released into the public domain
###

def load_senti(data, threshold=0.05):
    """
    load the sentiment data
    store it in a dictionary indexed by lemma
    discard if:
       * no lemma is found
       * |score| < threshold 
    return the dictionary
    """
    lsentiment = {}
    ssentiment = {}
    senti = dd(list)
    for l in open(data):
        (tag, lemma, score, scores) = l.strip().split('\t')
        score = float(score) / 100
        ## try to find the synset in wordnet
        try:
            ss = wn.synset_from_pos_and_offset(tag[-1],
                                               int(tag[:8]))

            if abs(score) > threshold:
                senti[ss].append(score)
            else:
                senti[ss].append(0.0)
            ### try to find the lemma in wordnet
            lem =  [l for l in ss.lemmas() if
                    l.name().lower() == lemma.replace(' ','_')]                 
            if len(lem)  == 1:
                if abs(score) > threshold:
                    lsentiment[lem[0]] = score
                else:
                    lsentiment[lem[0]] = 0.0
            else:
                #print(f"couldn't find {lemma} in {ss}")
                pass
        except:
            #print("couldn't find", tag, file=sys.stderr)
            pass
    for s in senti:
        #print(s, senti[s], np.mean(senti[s]))
        ssentiment[s] = np.mean(senti[s])
    ## return the average sentiment for each lemma,
    ## and for each synset
    return lsentiment, ssentiment

lsnt, ssnt = load_senti(sentidata)


print("""{} synsets have sentiment.
{} synsets have non-zero-sentiment.
{} synsets have positive sentiment.
{} synsets have negative sentiment.
""".format(len(ssnt),
           len([s for s in ssnt if ssnt[s] != 0]),
           len([s for s in ssnt if ssnt[s] > 0]),
           len([s for s in ssnt if ssnt[s] < 0]))) 

## Take a look at the data
# for l in lsnt:
#     if abs(lsnt[l]) > 0.05:
#         print (l, lsnt[l])
# for s in ssnt:
#     if abs(ssnt[s]) > 0.05:
#         print (s, ssnt[s])

def check_similar(ssnt):
    """
    find the average difference for all synsets related by the 
    'similar to' relation which have non-zero sentiment
    """
    diffs = []
    ## look at all the synsets we have sentiment for
    for s1 in ssnt:
        for s2 in s1.similar_tos():
            ## look at all synsets similar_to them
            if (s1 in ssnt) and  (s2 in ssnt) \
               and ssnt[s2] != 0.0 and ssnt[s1] != 0.0:
                ## keep only non-zero sentiments
                diff= abs(ssnt[s2] - ssnt[s1])
                diffs.append(diff)
                #print (s1, s2, diff)
    return sum(diffs)/len(diffs) # or np.mean(diffs)


sim_diff = check_similar(ssnt)
print("Average difference in non-zero sentiment for similar_to:",
      sim_diff)




