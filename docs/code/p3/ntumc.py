from collections import defaultdict as dd
import sqlite3
import json

corpusdb='/home/bond/dbs/2020-hg2002/final/eng.db'
#corpusdb='eng.good.db'
conn = sqlite3.connect(corpusdb)
c = conn.cursor()

def sents(did=440):
    """Return the sentences for a given docid (default 440)"""
    stype = dd(str)
                    
    c.execute("""SELECT sid, sent, comment 
    FROM sent WHERE docid=?
    ORDER BY sid""", (did,))  
    sents = list()
    for (sid, sent, comment) in c:
        sid = int(sid)
        if sid in (10000,):
            stype[sid]='h1'
        elif sid in (10001, 10006, 10008, 10010, 10011, 10017, 10018, 10021, 10027, 10028, 10029, 10034, 10037, 10038, 10040, 10041, 10045, 10053, 10054, 10060, 10064, 10065, 10066, 10068, 10074, 10080, 10084, 10087, 10090, 10091, 10096, 10097, 10098, 10104, 10105, 10109, 10110, 10111, 10112, 10114, 10118, 10120, 10122, 10123, 10125, 10127, 10128, 10129, 10131, 10133, 10155, 10157, 10159, 10160, 10162, 10165, 10171, 10172, 10173, 10174, 10175, 10176, 10177, 10178, 10180, 10181, 10182, 10190, 10192, 10193, 10195, 10196, 10198, 10199, 10201, 10202, 10206, 10209, 10211, 10212, 10214, 10216, 10219, 10223, 10224, 10225, 10226, 10227, 10228, 10229, 10230, 10231, 10232, 10233, 10237, 10241, 10242, 10243, 10244, 10246, 10250, 10251, 10252, 10253, 10257, 10258, 10259, 10260, 10261, 10264, 10271, 10272, 10275, 10278, 10280, 10290, 10296, 10297, 10299, 10300, 10301, 10302, 10304, 10306, 10307, 10311, 10315, 10317, 10318, 10319, 10321, 10325, 10330, 10331, 10333, 10335, 10337, 10341, 10343, 10345, 10351, 10358, 10359, 10360, 10361, 10362, 10363, 10365, 10371, 10372, 10373, 10376, 10378, 10381, 10382, 10383, 10384, 10386, 10389, 10390, 10391, 10393, 10395, 10396, 10398, 10400, 10402, 10406, 10410, 10412, 10413, 10415, 10419, 10421, 10422, 10423, 10425, 10426, 10427, 10428, 10431, 10432, 10434, 10435, 10438, 10439, 10440, 10441, 10442, 10443, 10444, 10445, 10446, 10447, 10451, 10456, 10458, 10459, 10460, 10461, 10462, 10464, 10466, 10467, 10468, 10470, 10471, 10472, 10477, 10478, 10481, 10482, 10483, 10484, 10486, 10487, 10489, 10491, 10497, 10499, 10500, 10502, 10504, 10505, 10508, 10510, 10516, 10517, 10519, 10520, 10523, 10524, 10527, 10534, 10540, 10542, 10545, 10549, 10550, 10553, 10556, 10563, 10565, 10567, 10571, 10572, 10575, 10589, 10595, 10596):
            stype[sid]='p'
        sents.append((sid, sent, stype[sid], comment))
    return sents

def tagged_words(did=440):
    """Return the sentences for a given docid (default 440)
    list of (sid, wid, word, pos, lemma, cid, clemma, tag, comment)"""
    ### get concept word link
    c.execute("""SELECT cwl.sid, cwl.wid, cwl.cid
    FROM (SELECT sid FROM sent WHERE docid=?
    ORDER BY sid) as sent
    JOIN cwl on sent.sid=cwl.sid""", (did,))  
    clink = dd(lambda: dd(list))
    for (sid, wid, cid) in c:
        clink[sid][wid].append(cid)

    c.execute("""SELECT sent.sid, cid, clemma, tag, comment
    FROM (SELECT sid FROM sent WHERE docid=?
    ORDER BY sid) as sent
    JOIN concept on sent.sid=concept.sid""", (did,))  
    concept = dd(lambda: dd())
    for (sid, cid, clemma, tag, comment) in c:
        if tag and tag not in  ['x', 'w', 'e']:  ### check 'w' and 'e' later
            ##print(sid, cid, clemma, tag, comment)
            concept[sid][cid] = (clemma, tag, comment)


    c.execute("""SELECT sent.sid, cid, score
    FROM (SELECT sid FROM sent WHERE docid=?
    ORDER BY sid) as sent
    JOIN sentiment on sent.sid=sentiment.sid""", (did,))  
    sentiment =  dd(lambda: dd())
    for sid, cid, score in c:
         sentiment[sid][cid] = score
            
    c.execute("""SELECT word.sid, wid, word, lemma, pos, word.comment
    FROM (SELECT sid FROM sent WHERE docid=?
    ORDER BY sid) as sent
    JOIN word on sent.sid=word.sid ORDER by word.sid, wid""", (did,))
  
    words = list()
    for (sid, wid, word, lemma, pos, comment) in c:
        ##print (sid, wid, word, lemma, pos, comment)
        ok_clemma = ''
        ok_cid = -1
        ok_tag = ''
        ok_sentiment = 0.0
        for cid in clink[sid][wid]:
            if cid in concept[sid]:
                (clemma, tag, comment) = concept[sid][cid]
                ok_clemma = clemma
                ok_cid = cid
                ok_tag = tag
            if cid in  sentiment[sid]:
                ok_sentiment = sentiment[sid][cid] / 100
        words.append((sid, wid,
                      word, lemma, pos,
                      ok_cid, ok_clemma, ok_tag, ok_sentiment,
                      comment))
    return words
    

data = sents()
with open('sents.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)


data =  tagged_words()
with open('words.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
