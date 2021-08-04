# -*- coding: utf-8 -*-
import re
import nltk
import random
import codecs
#from urllib import request
#f = request.urlopen('http://web.mysites.ntu.edu.sg/fcbond/open/pubs/enamdict').read().decode('utf-8')

### copy it locally to save time
f = codecs.open('enamdict', encoding='utf8', mode='r')


name = dict()
name['m'] = list()
name['f'] = list()
name['g'] = list()

#for line in f.splitlines():
for line in f:
        #print (line)
        ##Look for names
        ## あるこ /Aruko (f)/  ### we want あるこ f
        m = re.search(r'^(.*?) .*\(([fgm])\)/', line)
        if (m):
        #print ("@%s@@%s@" % (m.group(1), m.group(2)))
            name[m.group(2)].append(m.group(1))
            #print ( m.group(1), m.group(1)[-1])
        
### Also 'o' organization and 's' surname, ...
print ("%6d male names: %s" % (len(name['m']), ', '.join(random.sample(name['m'], 5))))
print ("%6d female names: %s" % (len(name['f']), ', '.join(random.sample(name['f'],5))))
print ("%6d unknown names: %s" % (len(name['g']), ', '.join(random.sample(name['g'],5))))

minlength = min(len(name['m']), len(name['f']))

### Balance the number of names (same number male and female)
#names = list()
names =  [(n, 'female') for n in random.sample(name['f'], minlength)] + \
    [(n, 'male') for n in random.sample(name['m'], minlength)]
#for name in random.sample(name['m'], minlength - 1):
#for n in name['m']:
#   names.append((n, 'male'))


print ("A random selection of names")
random.shuffle(names)
print ( '\n'.join([ "%s (%s)" % (n, t)  for (n, t) in names[:10] ]))

### define some features
def gender_features(word):
    return {'last_char': word[-1],
            'first_char':  word[0]}

featuresets = [(gender_features(n), g, n) for (n,g) in names]
for t in featuresets[:10]:
    print ("%s %s %s" % t)

### split into 90, 5, 5
size = int(.05*len(names))
train, dev, test = featuresets[18*size:], featuresets[18*size:19*size], featuresets[19*size:]

classifier = nltk.DecisionTreeClassifier.train([(f,g) for (f,g,n) in train])

print ("Dev Accuracy: ", nltk.classify.accuracy(classifier, [(f,g) for (f,g,n) in dev]))
print ("Test Accuracy: ", nltk.classify.accuracy(classifier, [(f,g) for (f,g,n) in test]))


errors = []
for (f, g, n) in dev:
    guess = classifier.classify(f)
    # if guess != g:
    #     print ("%s '%s' (%s = %s) %s" % (n ,f, g, guess, g==guess))
    if guess != g:
        errors.append((n, g, guess, f) )

### Some errors
print ("\nA sample of up to ten errors (from Dev):")
for (name, gender, guess, features) in sorted(errors[:10]): 
    print ('correct=%-8s guess=%-8s name=%-30s' % (gender, guess, name))



#Train a classifier that does Word Sense Disambiguation:

# The Senseval 2 Corpus contains data intended to train word-sense
# disambiguation classifiers. It contains data for four words: hard,
# interest, line, and serve. Choose one of these four words, and load
# the corresponding data:

from nltk.corpus import senseval
instances = senseval.instances('hard.pos')
size = int(0.9*len(instances))
train, test = instances[size:], instances[:size]

#print (train[:10])
# Using this dataset, build a classifier that predicts the correct
# sense tag for a given instance

# Hint: Here is how to look at the individual contexts

for inst in train[:5]:
    p = inst.position
    left = ' '.join(w for (w,t) in inst.context[p-2:p])
    word = ' '.join(w for (w,t) in inst.context[p:p+1])
    right = ' '.join(w for (w,t) in inst.context[p+1:p+3])
    senses = ' '.join(inst.senses)
    print ('%20s |%10s | %-15s -> %s' % (left, word, right, senses))
#        declines in |  interest | rates .         -> interest_6
# indicate declining |  interest | rates because   -> interest_6
#      in short-term |  interest | rates .         -> interest_6
#                4 % |  interest | in this         -> interest_5
#       company with | interests | in the          -> interest_5
#             , plus |  interest | .               -> interest_6
#            set the |  interest | rate on         -> interest_6
#             's own |  interest | , prompted      -> interest_4
#      principal and |  interest | is the          -> interest_6
#       increase its |  interest | to 70           -> interest_5
          


# Hint: useful features
#         one or two words on either side
#         one or two POSs on either side
#         Bag of words 


def features(instance):
    feat = dict()
    p = instance.position
       ## previous word and tag
    if p: ## > 0
        feat['wp'] = instance.context[p-1][0]
        feat['tp'] = instance.context[p-1][1]
       ## use BOS if it is the first word
    else: # 
        feat['wp'] = (p, 'BOS')
        feat['tp'] = (p, 'BOS')
       ## following word and tag       
        feat['wf'] = instance.context[p+1][0]
        feat['tf'] = instance.context[p+1][1]
    return feat


featureset =[(features(i), i.senses[0]) for i in 
             instances if len(i.senses)==1]

### shuffle them randomly
random.shuffle(featureset)

print (featureset[:2])
 # [({'tf': 'NNS', 'wf': 'rates', 'tp': 'IN', 'wp': 'in'}, 'interest_6'),
 # ({'tf': 'NNS', 'wf': 'rates', 'tp': 'VBG', 'wp': 'declining'},
 # 'interest_6')]

### try on a small sample
train, dev, test = featureset[500:], featureset[:250], featureset[250:500]
classifier = nltk.NaiveBayesClassifier.train(train)
print ("Accuracy on Dev:", nltk.classify.accuracy(classifier, dev))
#0.832
print ("Accuracy on Test:", nltk.classify.accuracy(classifier, train))
#0.832
