#Write a function shorten(text, n) to process a text,
# omitting the n most frequently occurring words of the text.
# How readable is it?
import nltk

def shorten(text, n):
    """Delete the most frequent n words from a text (list of words)"""
    assert isinstance(text, list), "The text should be a list of words"
    most_frequent_words = set(w for (w,f) in nltk.FreqDist(text).most_common(n))
    return [w for w in text if w not in most_frequent_words]


text = "to be or not to be that is the question".split()
out = "or not that is the question".split()
print(text)
print (shorten(text,0))
print (shorten(text,1))
print (shorten(text,1))
print (shorten(text,2))
##print shorten("to be or not to be that is the question", 2)


#Write a list comprehension that sorts a list of WordNet synsets
#for proximity to a given synset.
#For example, given the synsets for the first noun sense of  minke whale,
# orca novel and tortoise, sort them according to their shortest_path_distance()
# from right whale
import wn
from wn import similarity as sim

wn.download('oewn')
oewn = wn.Wordnet('oewn:2021')
 
comp = [oewn.synsets(s, pos='n')[0] for s in
          ["minke whale", "orca", "novel", "tortoise"]]

rightwhale = oewn.synsets('right whale', pos='n')[0]

print ("\n\n Unsorted")
for s in comp:
    print (s.id, s.definition())

def semantic_sort(sslist, ss):
    """
    return a list of synsets, sorted by similarity to another synset
    this method uses tuples to sort (a bit of a hack)
    """
    sims = [(sim.path(s, ss), s) for s in sslist]
    return [s for (sm, s) in sorted(sims)]

print ("\n\n Hacky sort")
for s in (semantic_sort(comp, rightwhale)):
    print (s.id, s.definition())

def semantic_sort1(sslist,ss):
    """
    return a list of synsets, sorted by similarity to another synset
    this uses a lambda function as the key to sort
    """
    return sorted(sslist, key=lambda x: sim.path(ss,x))     

print ("\n\n Pythonesque sort")   
for s in (semantic_sort1(comp, rightwhale)):
    print (s.id, s.definition())



# Write a function that takes a list of words (containing duplicates)
#  and returns a list of words (with no duplicates) sorted by
#  decreasing frequency.
#  E.g. if the input list contained 10 instances of the word table and
#  9 instances of the word chair, then table would appear before chair
#  in the output list.


           
def dec_freq(liszt):
    """
    take a list and returns a list of types in decreasing frequency
    uses the Frequency Distribution from NLTK
    """
    FD = nltk.FreqDist(liszt)
    return sorted(FD.keys(), key =lambda x: -FD[x])

#
# from scratch
#        
def dec_freq1(liszt):
    """
    take a list and returns a list of types in decreasing frequency
    """
    freq = dict()
    for l in liszt:
        if l in freq:
           freq[l] += 1
        else:
           freq[l] = 1
    return sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

print ("\n\n Sort by frequency in list (two ways)\n\n")   

test = 'two two one three four three four three ten four ten ten four ten ten ten ten ten ten ten'.split()

print(dec_freq(test))

print(dec_freq1(test))       
           
#  Write a program to sort words by length.
#
print ("\n\n Sort words by length (two ways)\n\n")   

print (sorted(test, key=lambda  x:len(x)))
print (sorted(test, key=len))
