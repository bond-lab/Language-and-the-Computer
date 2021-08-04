### *-* encoding: utf-8 -*-
### baseline regular expression tagger
###

import nltk
tagged = nltk.corpus.treebank.tagged_sents()

print (tagged[:1])

ln =  int(0.9*len(tagged))
train = tagged[:ln]
test = tagged[ln:]

### Train and evaluate a bigram tagger with a data set transformed to
### use explicit unknown words. How well does it perform?

# calculate the frequency
### We should really only look at words in train to calculate the frequency
trainwords = list()
for s in train:
    for (w,t) in s:
        trainwords.append(w)
wfd = nltk.FreqDist(trainwords)


def unkme (word, fd, threshold):
    "if the frequency <= threshold, return 'UNK' otherwise return the word"
    if fd[word] <= threshold:
        return "UNK"
    else:
        return word

for tau in range(5): # τ 'standard symbol for a threshold'
    print ("\nCalculating a model with threshold for unknowns set to %d" % tau)
    ## replace low frequency words in both test and train
    trainu= [[(unkme(w,wfd,tau), t) for (w,t) in s] for s in train]
    testu=[[(unkme(w,wfd,tau), t) for (w,t) in s] for s in test]

    print ("\nBigram Tagger with no backoff")
    bigram_tagger = nltk.BigramTagger(trainu)
    print ("Accuracy on Test: ", bigram_tagger.evaluate(testu))

    unigram_tagger=nltk.UnigramTagger(trainu)
    bigram_tagger = nltk.BigramTagger(trainu, backoff=unigram_tagger)
    print ("\nBigram Tagger with backoff to Unigram")
    print ("Accuracy on Test: ", bigram_tagger.evaluate(testu))

print ("\n\n")

### Consider the regular expression tagger described in Section
### 5.4. Evaluate the tagger using its accuracy() method, and try to
### come up with ways to improve its performance. Discuss your
### findings. How does objective evaluation help in the development
### process?

patterns = [      
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'.*', 'NN') ]
regexp_tagger = nltk.RegexpTagger(patterns)

print ("Accuracy of Regexp Tagger on Test: ", regexp_tagger.evaluate(test))
#0.24244274809160304

### add NNP for capitalized words
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'[A-Z].*', 'NNP'),  
    (r'.*', 'NN') ]

regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.evaluate(test)
0.32335877862595419

### add NNP first
patterns = [    
    (r'[A-Z].*', 'NNP'),
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'.*', 'NN') ]
regexp_tagger = nltk.RegexpTagger(patterns)
print ("Accuracy of Regexp Tagger (with Capitals) on Test: ", regexp_tagger.evaluate(test))
#0.32885496183206109


### how to find out more about the tags
#nltk.help.upenn_tagset()

#nltk.help.brown_tagset()
