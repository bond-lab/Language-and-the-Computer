###
### set up
###
import nltk
from nltk.corpus import gutenberg


print("How many words (tokens) are there in Jane Austen's novel Persuasion?")
print(len(gutenberg.words("austen-persuasion.txt")))
print() 
print("How many times does the word persuasion occur?")
print(gutenberg.words("austen-persuasion.txt").count("persuasion"))
print(gutenberg.words("austen-persuasion.txt").count("Persuasion"))
print("Make a concordance for 'persuasion' in the novel.")
per = nltk.Text(gutenberg.words("austen-persuasion.txt"))
per.concordance("persuasion")
print()
print()
print("How many characters (including punctuation and spaces) are there in the novel?") 
print(len(gutenberg.raw("austen-persuasion.txt")))
print()
print("How many 'sentences' are there?") 
print(len(gutenberg.sents("austen-persuasion.txt")))
print()
print("Find and print the longest sentence(s).")
longest = max([len(s) for s in gutenberg.sents("austen-persuasion.txt")])
print([s for s in gutenberg.sents("austen-persuasion.txt") if (len(s) == longest)])

print()
print()

print('Make a frequency distribution for the "news" category of the Brown Corpus.') 
from nltk.corpus import brown

### Simple:
# bnfd = nltk.FreqDist(brown.words(categories="news"))
### better
bnfd = nltk.FreqDist(w.lower() for w  in brown.words(categories="news"))
print()
print("Print counts of the modal verbs: 'can, could, may, might, must, will'") 
modals = 'can, could, may, might, must, will'.split(', ')
for m in modals:
    print(m, bnfd[m])
print()
print("Print counts of the wh-words: what, when, where, who, how, why.") 
whs = ["what", "when", "how", "why", "where", "who" ]
for m in whs:
    print(m, bnfd[m])
print()

print('Make a frequency distribution for the "romance" category.')
brfd = nltk.FreqDist(w.lower() for w  in brown.words(categories="romance"))

print()
print("Print counts of the modal verbs and the wh-words.") 
print("Compare the counts for the two genres. Are there any clear differences?\n") 
print("Word    News  Romance")
for w in modals+whs:
	print(f"{w:5} {bnfd[w]:7d} {brfd[w]:7}")

print()
print("Better to normalize for comparison (divide by number of words)")
print("%-5s: %7s %7s (in words/thousand)" % ('word', 'news',  'rom'))
for w in modals+whs:
	print(f"{w:7}  {1000.0* bnfd[w] / bnfd.N():5.3}   {1000.0*brfd[w] / brfd.N():5.3}")

print()
print("Swadesh Lists")
swen = nltk.corpus.swadesh.words('en')
swde = nltk.corpus.swadesh.words('de')
swfr = nltk.corpus.swadesh.words('fr')

for i in range(len(swen)):
    ## easier
    print("; ".join([swen[i], swde[i], swfr[i]]))


### even pythonier
###
### use zip to zip lists together
### use format to make them line up nicely
###
print()
print("In the best python style:")
print()
for sw in zip(swen, swde, swfr):
     print("%-20s %-20s %-20s" % sw)
