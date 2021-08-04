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
#For example, given the synsets minke_whale.n.01, orca.n.01, novel.n.01,
# and tortoise.n.01, sort them according to their shortest_path_distance()
# from right_whale.n.01

from nltk.corpus import wordnet as wn
whales = [wn.synset(s) for s in
          "minke_whale.n.01, orca.n.01, novel.n.01, tortoise.n.01".split(', ')]
print (whales)

def semantic_sort(sslist,ss):
    """return a list of synsets, sorted by similarity to another synset"""
    sim = [(ss.shortest_path_distance(s), s) for s in sslist]
    return [s for (sm, s) in sorted(sim)]

print (semantic_sort(whales, wn.synset('right_whale.n.01')))

def semantic_sort1(sslist,ss):
    """return a list of synsets, sorted by similarity to another synset"""
    return sorted(sslist, key=lambda x: ss.shortest_path_distance(x))     
    
print (semantic_sort1(whales, wn.synset('right_whale.n.01')))



# Write a function that takes a list of words (containing duplicates)
#  and returns a list of words (with no duplicates) sorted by
#  decreasing frequency.
#  E.g. if the input list contained 10 instances of the word table and
#  9 instances of the word chair, then table would appear before chair
#  in the output list.

def dec_freq(liszt):
    """take a list and returns a list of types in decreasing frequency"""
    return list(nltk.FreqDist(liszt).keys())

#  Write a program to sort words by length.
#  

print (sorted(text, key=lambda  x:len(x)))
print (sorted(text, key=len))
