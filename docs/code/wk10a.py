## Train a bigram tagger with no backoff tagger, and run it on some of
## the training data. Next, run it on some new data. What happens to
## the performance of the tagger? Why?
      

import nltk
tagged = nltk.corpus.treebank.tagged_sents()

print (tagged[:1])

ln =  int(0.9*len(tagged))
train = tagged[:ln]
test = tagged[ln:]

print ("Training Bigram Tagger")
bigram_tagger = nltk.BigramTagger(train)

print (bigram_tagger.tag(nltk.word_tokenize('The police reported it.')))

print (bigram_tagger.tag(nltk.word_tokenize('The police saw the report.')))

print ("Accuracy on Test: ", bigram_tagger.evaluate(test))
#0.13475826972010177
print ("Accuracy on Train:", bigram_tagger.evaluate(train))
#0.91111820453269643

### Now add a backoff tagger (your choice) and try it again (build
### then evaluate). What happens to the performance of the tagger this
### time and why?

print ("\nTraining Unigram Tagger")
backoff_tagger=nltk.UnigramTagger(train)

print ("Accuracy on Test: ", backoff_tagger.evaluate(test))
#0.86493638676844786

print ("Accuracy on Train:", backoff_tagger.evaluate(train))
#0.96015453875026147

print ("\nTraining Bigram Tagger with backoff to unigram")
bigram_tagger = nltk.BigramTagger(train, backoff=backoff_tagger)

print ("Accuracy on Test: ", bigram_tagger.evaluate(test))
#0.87430025445292625

print ("\nTraining Bigram Tagger with backoff to NNP (Proper Noun)")
backoff_tagger=nltk.DefaultTagger('NNP')
unigram_tagger=nltk.UnigramTagger(train, backoff=backoff_tagger)
bigram_tagger = nltk.BigramTagger(train, backoff=unigram_tagger)
print ("Accuracy on Test (bigram/NNP): ", bigram_tagger.evaluate(test))
#0.89954198473282443

print ("\nTraining Bigram Tagger with backoff to NN (Common Noun)")
backoff_tagger=nltk.DefaultTagger('NN')
unigram_tagger=nltk.UnigramTagger(train, backoff=backoff_tagger)
bigram_tagger = nltk.BigramTagger(train, backoff=unigram_tagger)
print ("Accuracy on Test (bigram/NN):", bigram_tagger.evaluate(test))
# 0.89251908396946567

print ("\nTraining Bigram Tagger with backoff to NNP (Proper Noun)")
backoff_tagger=nltk.DefaultTagger('NNP')
unigram_tagger=nltk.UnigramTagger(train, backoff=backoff_tagger)
bigram_tagger = nltk.BigramTagger(train, backoff=unigram_tagger)
trigram_tagger = nltk.TrigramTagger(train, backoff=bigram_tagger)

print ("Accuracy on Test (trigram/NNP): ", trigram_tagger.evaluate(test))

fourgram_tagger = nltk.NgramTagger(4, train, backoff=trigram_tagger)

print ("Accuracy on Test (4gram/NNP): ", fourgram_tagger.evaluate(test))

perceptron_tagger = nltk.PerceptronTagger(train)

print ("Accuracy on Test (Perceptron): ", perceptron_tagger.evaluate(test))






#0.89954198473282443



## NNP is the better backoff
