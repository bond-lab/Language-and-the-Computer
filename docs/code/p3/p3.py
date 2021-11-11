from collections import defaultdict as dd
import json
import wn

### you can comment out the download to be faster
#wn.download('https://github.com/omwn/omw-data/releases/download/v1.4/omw-en-1.4.tar.xz')
wn = wn.Wordnet(lexicon='omw-en:1.4')
prefix='omw-en'
##
## Change me!
##
title = "Skeleton Solution"
author = "Francis Bond"
outfile = 'p3.html'

##
## Read in the data
##
with open('sents.json') as f:
  sents = json.load(f)
with open('words.json') as f:
  words = json.load(f)

##
## get sentence type
##
stype = dd(str)
for (sid, sent, st, comment) in sents:
    stype[sid] = st

    
def print_head(fh,title=title):
    """
    print the HTML header, with title
    """
    print (f"""
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>{title}</title>
</head>
    <body>""".format(title), file=fh)


    
def print_foot(fh, title=title, by=author):
    """
    print the HTML footer, with title and author
    """
    print(f"""
<hr>
    <p>{title} produced by {by}
</body>
</html>
    """, file=fh)

def print_stype_pre(st,fh):
    """
    Print header and paragraph starts
    """
    if st == 'p':
        print ("<p>", file = fh)
    elif st == 'h1':
        print ("<h1>", file = fh)

def print_stype_post(st,fh):
    """
    Print header ends (assume one sentence long)
    """
    if st == 'h1':
        print ("</h1>", file = fh)

def tag2ss(tag):
    """
    map the tag to the wordnet (assuming the names match)
    """
    try:
        ss = wn.synset(id = f'{prefix}-{tag}')
    except:
        try:
            ss = wn.synset(id = f'{prefix}-{tag}'.replace('-a', '-s'))
        except:
            return None
    return ss
   

###
###  Print out the html
###

###
### you may want some new definitions to add style
###

with open(outfile, 'w', encoding='utf-8') as out:
    print_head(out)
    for (sid, wid, word, lemma, pos, cid, clemma, tag, sentiment, comment) in words:
        if wid == 0: # new sentence
            print_stype_post(stype[sid-1],out)
            print_stype_pre(stype[sid],out)
        ### This prints out the words

        ### *** Change at least here ***
        dfn = ''
        if tag2ss(tag):
            dfn=tag2ss(tag).definition()
        ###    title makes hover text
        ###    &#10; puts a newline in the hover text
        print (f"<span title='{pos}&#10;{tag}: {dfn}'>{word}</span> ", 
               file=out)
        ### 
    print_foot(out)
#print(words)


