import wn

wn.download('https://github.com/omwn/omw-data/releases/download/v1.4/omw-en-1.4.tar.xz')
wn = wn.Wordnet(lexicon='omw-en:1.4')
prefix='omw-en'
sentidata = "ntumc-NTUMC-senti.tsv"

def clean_senti(data, threshold=0.05, debug=False):
    """
    load the sentiment data
    store it in a dictionary indexed by lemma
    discard if:
       * no lemma is found
       * |score| < threshold 
    return the dictionary
    based on the fact that we know 'omw-en' uses similar IDs as the corpus
    """
    lsentiment = dict()
    for l in open(data):
        (tag, lemma, score, scores) = l.strip().split('\t')
        score = float(score) / 100
        ## try to find the synset in wordnet
        try:
            ss = wn.synset(id = f'{prefix}-{tag}')
        except:
            try:
                ss = wn.synset(id = f'{prefix}-{tag}'.replace('-a', '-s'))
            except:
                if debug:
                    print("couldn't find synset", tag)
                continue
        ### try to find the lemma in wordnet
        senses = set()
        for s in ss.senses():
            #print(s)
            for f in s.word().forms():
                #print(f'{f}')
                f = f.replace('(a)', '')
                f = f.replace('(p)', '')
                if f.lower() in [lemma,
                                 lemma.lower(),
                                 lemma.lower().replace(' ','_'),
                                 lemma.lower().replace('-','_'),
                                 lemma.lower().replace('-',''),
                                 lemma.lower().replace('-',' '),
                                 lemma.lower().replace(' ','')]:
                    #print('FOUND')
                    senses.add(s)
        #print(f'{senses=}')
        try:
            match = senses.pop()
            #print(f'LEM {len(senses)} {match} {senses}')
        except:
            if debug:
                print(f"couldn't find '{lemma}' in {ss}")
                print ([x.word().lemma() for x in ss.senses()])
            continue
        if abs(score) > threshold:
            lsentiment[match.id] = score
        else:
            lsentiment[match.id] = 0.0
        if len(senses) > 0:
            if debug:
                print(f"multi {senses}")
    return lsentiment




if __name__ == "__main__":
    lsentiment = clean_senti(sentidata, debug=False)

    for s in lsentiment:
        print(s, lsentiment[s], sep='\t') 
