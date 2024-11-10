### Tokenization
import spacy
import spacy_udpipe

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

udpipe_models = ['cs', 'id']
for lang in udpipe_models:
  spacy_udpipe.download(lang) # download model

for lang in udpipe_models:
  print(f'loading {lang}')
  nlp[lang] = spacy_udpipe.load(lang)

testdata = {
    "zh": "有时，敏捷的棕色狐狸跳过了懒惰的猫。多么令人兴奋啊！",          # Chinese
    "cs": "Někdy, rychlá hnědá liška přeskočí línou kočku. Jak vzrušující!",  # Czech
    "ja": "時々、素早い茶色の狐が怠けた猫を飛び越える。なんて素晴らしい！",    # Japanese
    "ko": "때때로, 빠른 갈색 여우가 게으른 고양이를 뛰어넘는다. 정말 신난다!",      # Korean
    "id": "Kadang-kadang, rubah cokelat cepat melompati kucing malas. Betapa seru!", # Indonesian
    "en": "Sometimes, the quick brown fox jumps over the lazy cat. How exciting!"  # English
}

#from spacy import displacy

for lang, sample in testdata.items():
  print(f"\nLanguage: {lang.upper()}")
  doc = nlp[lang](sample)
  for sent in doc.sents:
    #displacy.render(sent)
    print ('---')
    for token in sent:
      print(token.text, token.pos_,token.lemma_, token.morph, sep='\t')
  

      
