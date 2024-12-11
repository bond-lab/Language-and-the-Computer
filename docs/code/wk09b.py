### Tokenization
import spacy
import spacy_udpipe
import json

###
### Download models spacy has
###

spacy_models = {'zh':"zh_core_web_sm",
                "ja": "ja_core_news_sm",
                "ko": "ko_core_news_sm",
                "en": "en_core_web_sm"}
# download models
for model in spacy_models.values():
  spacy.cli.download(model)


nlp=dict()
for lang, model in spacy_models.items():
  nlp[lang]= spacy.load(model)

###
### Download models from upipe
###

udpipe_models = ['cs', 'id', 'vi']
for lang in udpipe_models:
  spacy_udpipe.download(lang) # download model

for lang in udpipe_models:
  print(f'loading {lang}')
  nlp[lang] = spacy_udpipe.load(lang)

  
import nltk
nltk.download('udhr2')
### I printed out the files and then searched by hand!
print (nltk.corpus.udhr.fileids())
udhr_lang = {
    'en':'English-Latin1',
    'cs':'Czech-UTF8',
    'id':'Indonesian-Latin1',
    'zh':'Chinese_Mandarin-GB2312',
    'ko':'Korean_Hankuko-UTF8',
    'ja':'Japanese_Nihongo-UTF8',
    'vi':'Vietnamese-UTF8'
  }

stats = dict()

for lang, fileid in udhr_lang.items():
  lstats = dict()
  declaration = nltk.corpus.udhr.raw(fileid)
  doc = nlp[lang](declaration)
  lstats['sents'] = len(list(doc.sents))
  ### count the POS
  for t in doc:
    if t.pos_ in lstats:
      lstats[t.pos_].append(t.pos_)
    else:
       lstats[t.pos_] = []
  stats[lang] = lstats

UPOS = "ADJ ADV NOUN VERB PROPN INTJ ADP AUX CCONJ SCONJ DET NUM PART PRON PUNCT SYM X".split()

print()
print('Crosslingual Comparison')
print()
print('POS',  end='\t')
print('\t'.join(stats.keys()))
for thing in ['sents']  + UPOS:
  print(thing, end='\t')
  for lang in stats:
    if thing == 'sents':
      print(stats[lang][thing],  end='\t')
    else:
      if thing in stats[lang]:
        print(len(stats[lang][thing]), end='\t')
      else:
        print(0,  end='\t')
  print()

### print some data to be used later

print("\n\nFor week 11\n\n")

stats2 = dict()
for lang in stats:
  stats2[lang] = dict()
  for thing in UPOS:
    stats2[lang][thing] = len(stats[lang][thing]) if thing in stats[lang] else 0
    
with open('udhr_pos.json', 'w') as out:
  json.dump(stats2, out)
