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
    stype[str(sid)] = st

    
def print_head(fh,title=title):
    """
    print the HTML header, with title
    Use boostrap for margins and such
    Use a serif font
    """
    print (f"""
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <!-- Bootstrap CSS -->
  <link rel="stylesheet"
	href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
	integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
	crossorigin="anonymous">
  <style>
    body {{
    font-family:  serif;
    }}
  </style>
</head>
  <body class="container">
    <div class="column">
""", file=fh)


    
def print_foot(fh, title=title, by=author):
    """
    print the HTML footer, with title and author
    """
    print(f"""
<hr>
    <p>{title} produced by {by}
</div>
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
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
            print(f"Could not find '{prefix}-{tag}'")
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
    for sid in words:
      ## Open sentence type
      print_stype_pre(stype[sid],out)
      for (wid, word, lemma, pos, cid, clemma, tag, sentiment,
           comment) in words[sid]:
        ### This prints out the words

        ### *** Change at least here ***
        dfn = ''
        if tag and tag2ss(tag):
          dfn=tag2ss(tag).definition()
        ###    title makes hover text
        ###    &#10; puts a newline in the hover text
        print (f"<span title='{pos}&#10;{tag}: {dfn}'>{word}</span> ", 
               file=out)
      ### Close off paragraph type
      print_stype_post(stype[sid],out)

    print_foot(out)
#print(words)


