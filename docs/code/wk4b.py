# -*- encoding: utf-8 -*-
# <li> <u>Comparing authors</u> 
#     <ol>
#       <li>Make a frequency distribution for Jane Austen's novel
# 	<i>Persuasion</i>. 
#       <li>Print counts of the modal verbs
# 	<i>can, could, may, might, must, will</i>. 
#       <li>Print counts of the personal pronouns
# 	<i>he, him, himself, she, her, herself</i>. 
#       <li>Make a frequency distribution for Herman Melville's novel
# 	<i>Moby Dick</i>. 
#       <li>Print counts of the modal verbs and the personal pronouns. 
#   <li>Compare the counts for the two authors. Are there any clear
# 	differences?

import nltk
from nltk.corpus import gutenberg
##
## Using Dictionaries
##
books = ['austen-persuasion.txt', 'melville-moby_dick.txt']
stats = dict()
words =dict()

for f in books:
  print(f)
  words[f] = nltk.corpus.gutenberg.words(f)
  stats[f] = nltk.FreqDist(words[f])

modals = "can, could, may, might, must, will".split(', ')

for m in modals:
  print(f"{m:10} {100*stats[books[0]][m]/len(words[f]):5.3f}  {100*stats[books[1]][m]/len(words[f]):5.3f}")

##
## Using Conditional Frequency Distribution
##

pers = gutenberg.words('austen-persuasion.txt')
cpers = [('Austen', w) for w in pers]
moby = gutenberg.words('melville-moby_dick.txt')
cmoby = [('Melville', w) for w in moby]
cfd = nltk.ConditionalFreqDist(cpers+cmoby)
print("\nModals\n")
cfd.tabulate(conditions=cfd.conditions(), 
             samples="can, could, may, might, must, will".split(', '))
print("\nPronouns\n")
cfd.tabulate(conditions=cfd.conditions(), samples='he him himself she her herself'.split())
###
### Note better to normalize
###


def sim (w1, w2):
    "this takes two words and returns a similarity between 0 and 1 inclusive"
    w1 = w1.lower()
    w2 = w2.lower()
    inboth= set()
    ineither= set()
    for c1 in w1:
        for c2 in w2:
            if c1==c2:
                inboth.add(c1)
    ineither= set(w1+w2)
    #print(w1,w2,inboth,ineither)
    ## | w1  ∩  w2| / |w1 ∪  w2| 
    return len(inboth) / len(ineither)


def sim_set (w1, w2):
    "this takes two words and returns a similarity between 0 and 1 inclusive"
    w1 = w1.lower()
    w2 = w2.lower()
    ## | w1  ∩  w2| / |w1 ∪  w2| 
    return len(set(list(w1)).intersection(set(list(w2)))) \
        / len(set(list(w1+w2)))


# for (w1, w2) in [('the', 'the'), ('The', 'the'),
#                      ('the', 'der'), ('the', 'sono')]:
#     print w1, w2, sim(w1,w2)


def comp (l1, l2):
     sw1 = nltk.corpus.swadesh.words(l1)
     sw2 = nltk.corpus.swadesh.words(l2)
     if len(sw1) != len(sw2):
         return -1
     total = 0
     for i in range(len(sw1)):
         total = total + sim(sw1[i], sw2[i])
     return 1.0* total/len(sw1)

print("Compare everything with everything")
### could check to see if we have compared this pair before

for l1 in nltk.corpus.swadesh.fileids():
    for l2 in nltk.corpus.swadesh.fileids():
        if l1 != l2: #pointless to compare against ourselves
            print("%3s %3s %0.3f" % (l1, l2, comp(l1,l2)))


maxsim = max(comp(l1,l2) for l1 in nltk.corpus.swadesh.fileids() \
              for l2 in nltk.corpus.swadesh.fileids() if l1 !=l2)

print("Highest similarity is", maxsim)
print("For: ", end=' ') 
print([(l1, l2) for l1 in nltk.corpus.swadesh.fileids() \
           for l2 in nltk.corpus.swadesh.fileids() \
           if comp(l1,l2) == maxsim])




# <li>
#   Using IDLE as an editor, as shown in
#   <a href="http://nltk.googlecode.com/svn/trunk/doc/book/ch02.html#more-python-reusing-code">
#     More Python: Reusing Code</a>,
#   write a Python program  <code>generate.py</code>
#   to do the following. 
# <ol>
# <li>In
#   <a href="http://nltk.googlecode.com/svn/trunk/doc/book/ch02.html#generating-random-text-with-bigrams">
#     Generating Random Text with Bigrams</a>,
#   a function <b><tt>generate_model()</b></tt> is defined. Copy this function
#   definition exactly as shown.
# </li>
import nltk, random

def generate_model(cfdist, word='Once' , num=15):
    for i in range(num):
        print(word, end=' ')
        ##word = cfdist[word].max()
        word = random.choice(list(cfdist[word].keys()))
    print() ## finish with a newline

texte = nltk.corpus.gutenberg.words('austen-emma.txt')
bigramse = nltk.bigrams(texte)
cfde = nltk.ConditionalFreqDist(bigramse)
textm = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
bigramsm = nltk.bigrams(textm)
bigramsem = nltk.bigrams(texte+textm)
cfdm =  nltk.ConditionalFreqDist(bigramsm)
cfdem = nltk.ConditionalFreqDist(bigramsem)

print("Random Emma")
generate_model(cfde,word='The',num=35)
print()
print("Random Moby")
generate_model(cfdm,word='The',num=35)
print()
print("Random Emma and Moby")
generate_model(cfdem,word='The',num=35)
print()
print("Random Emma and Moby with defaults")
generate_model(cfdem)
print()


