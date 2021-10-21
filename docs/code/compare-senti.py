#
# read each lexicon into a dictionary of sent[word] = score
# normalize to between -1 and 1
#
from collections import defaultdict as dd

def slurp_DAL():
    data = 'en_senti/DAL/DictionaryofAffect'
    fh = open(data)
    rawdata = fh.read()
    data = rawdata[893:481772] # ---- to end data
    valence = dict()
    for l in data.splitlines():
        (word, sentiment, activation, imagery) = l.strip().split()
        valence[word] = float(sentiment) - 2
    return valence

def slurp_AFINN():
    data = 'en_senti/AFINN/AFINN-111.txt'
    fh = open(data)
    valence = dict()
    for l in fh:
        (word, sentiment) = l.strip().split('\t')
        valence[word] = int(sentiment) /5.0
    return valence

def slurp_GLAS():
    data = 'en_senti/GLASGOW/13428_2018_1099_MOESM2_ESM.csv'
    fh = open(data)
    valence = dict()
    for l in fh:
        (word, length,
         AROU_M, AROU_SD, AROU_N,
         VAL_M, VAL_SD, VAL_N,
         DOM_M, DOM_SD, DOM_N,
         CNC_M, CNC_SD, CNC_N,
         IMAG_M, IMAG_SD, IMAG_N,
         FAM_M, FAM_SD, FAM_N,
         AOA_M, AOA_SD, AOA_N,
         SIZE_M, SIZE_SD, SIZE_N,
         GEND_M, GEND_SD, GEND_N) = l.strip().split(',')
        if word and word !='Words':
            valence[word] = (float(VAL_M) - 5) /5.0
            # 1--9
    return valence

def slurp_VADER():
    data = 'en_senti/VADER/vader_lexicon.txt'
    fh = open(data)
    valence = dict()
    for l in fh:
        (word, sentiment, std, scores) = l.strip().split('\t')
        valence[word] = float(sentiment) /4.0
    return valence

afinn = slurp_AFINN()
dal =  slurp_DAL()
glas = slurp_GLAS()
vader = slurp_VADER()


vocab = sorted(set(list(dal.keys()) + list(afinn.keys()) +
                   list(glas.keys()) + list(vader.keys())))
for w in vocab:
    dl = f'{dal[w]:+.2f}' if w in dal else '---'
    af =  f'{afinn[w]:+.2f}' if w in afinn else  '---'
    gl =  f'{glas[w]:+.2f}' if w in glas else  '---'
    vd =  f'{vader[w]:+.2f}' if w in vader else  '---'
    print(f'{w:30s}', dl, af, gl, vd, sep ='\t')
