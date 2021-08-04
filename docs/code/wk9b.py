#    Working with someone else, take turns to pick a word that can be
#    either a noun or a verb (e.g. contest); the opponent has to
#    predict which one is likely to be the most frequent in the Brown
#    corpus; check the opponent's prediction, and tally the score over
#    several turns.

import nltk
bw = nltk.corpus.brown.words()
bwt = nltk.corpus.brown.tagged_words()
bwts = nltk.corpus.brown.tagged_words(tagset='universal')


##
## count tags per word
##
wtc = nltk.defaultdict(lambda: nltk.defaultdict(int))
for (w,t) in bwts:
    wtc[w][t] +=1

print ("\nParts of Speech per word\n")
print ('contest', wtc['contest'].items())

# Guess which word is most likely to follow n-grams and test your intuition with the Brown corpus
#     for the
#     said that
#     it was
#     at the same
#     from time to 

### remember n grams, nd coutn the following word

for i in range(2,5):
	for ngram in nltk.ngrams(bw,i):
		wtc[ngram[:i-1]][ngram[i-1]] +=1

for w in ['for the', 'said that', 'it was', 'at the same', 'from time to']:
    print (w, wtc[tuple(w.split())].items())

#    Use sorted() and set() to get a sorted list of tags used in the
#    Brown corpus, removing duplicates.

print ("\nBrown corpus Tags, sorted alphabetically\n")
tags = sorted(set([t for (w,t) in bwt]))
for t in tags:
    print (t)

print ("\nBrown corpus Universal Tags, sorted alphabetically\n")
tags = sorted(set([t for (w,t) in bwts]))
for t in tags:
    print (t)


##Write programs to process the Brown Corpus and find answers to the following questions:
#        Which nouns are more common in their plural form, rather than
#        their singular form? (Only consider regular plurals, formed
#        with the -s suffix.)
freq = nltk.defaultdict(int)
for w in [w.lower() for (w,t) in bwt if t.startswith('N')]:
    freq[w] +=1
print ("\nWhich Nouns are more common as plural?\n")
for w in freq:
    if w+'s' in freq and freq[w+'s'] > freq[w]:
        print ("%s (%d, %d)" % (w, freq[w+'s'], freq[w]))


#        Which word has the greatest number of distinct tags. What are they, and what do they represent?

print ("\nWord with the most distinct tags\n")
word_tag = nltk.defaultdict(set)
for w,t  in  bwt:
    word_tag[w.lower()].add(t)
m = max(len(word_tag[w]) for w in word_tag)
print  ([(w, t) for w,t  in word_tag.items() if len(t) == m])

#        List tags in order of decreasing frequency. What do the 20 most frequent tags represent?
print ("\nTop 20 tags in decreasing frequency\n")

tagfd = nltk.FreqDist(t for (w,t)  in  bwt)
print (tagfd.most_common(20))

print ("\nTop 20 simplified tags in decreasing frequency\n")

tagfd = nltk.FreqDist(t for (w,t)  in  bwts)
print (tagfd.most_common(20))

#        Which tags are nouns most commonly found after? What do these tags represent? 

print ("\nTop 20 simplified tags that proceed nouns\n")
tagbigram =nltk.bigrams(t for (w,t)  in  bwts)

afterN = nltk.FreqDist(t1 for (t1,t2)  in  tagbigram if t2 == 'NOUN')

print (afterN.most_common(20))

