
import re

def swear_filter(text, censor_type='full'):
    """
    Censors offensive words in a text by replacing them with asterisks or alternatives.
    
    Parameters:
        text (str): The text to censor.
        censor_type (str): 'full' (replace all letters with *),
                           'partial' (replace all letters except 1st and last),
                           'bleep' (replace short words with 'bleep' and long words with 'bleepbleep').
                           
    Returns:
        str: The censored text.
        
    Example:
        >>> swear_filter("You are a shit")
        'You are a ****'
        >>> swear_filter("You are a shit", censor_type='partial')
        'You are a s**t'
        >>> swear_filter("You are a shit", censor_type='bleep')
        'You are a bleep'
        >>> swear_filter("You are a motherfucker", censor_type='bleep')
        'You are a bleepbleep'
        >>> swear_filter("Fuck you!")
        '**** you!'
        >>> swear_filter("Scunthorpe")
        'Scunthorpe'
    """
    ### check long words first!
    offensive_words = ["cocksucker", "motherfucker",
                       "shit", "piss", "fuck", "cunt", "tits"]
    censored_text = text

    def replacement(word):
        if censor_type == 'full':
            replacement = '*' * len(word)
        elif censor_type == 'partial':
            replacement = word[0] + '*' * (len(word) - 2) + word[-1]
        elif censor_type == 'bleep':
            if  len(word) > 4:
                replacement =  'bleepbleep'
            else:
                replacement = 'bleep'
        return replacement

            
    for word in offensive_words:
        censored_text = re.sub(f'\\b{word}\\b', replacement(word),
                               censored_text, flags=re.IGNORECASE)

    
    return censored_text

##
## Another version, that does better with 
##  partial matches of different capitalization



def swear_filter(text, censor_type='full'):
    """
    Censors offensive words in a text by replacing them with asterisks or alternatives.
    
    Parameters:
        text (str): The text to censor.
        censor_type (str): 'full' (replace all letters with *),
                           'partial' (replace all letters except 1st and last),
                           'bleep' (replace short words with 'bleep' and long words with 'bleepbleep').
                           
    Returns:
        str: The censored text.
        
    Example:
        >>> swear_filter("You are a shit")
        'You are a ****'
        >>> swear_filter("You are a shit", censor_type='partial')
        'You are a s**t'
        >>> swear_filter("You are a shit", censor_type='bleep')
        'You are a bleep'
        >>> swear_filter("You are a motherfucker", censor_type='bleep')
        'You are a bleepbleep'
        >>> swear_filter("I live in Scunthorpe", censor_type='bleep')
        'I live in Scunthorpe'
        >>> swear_filter("Fuck!", censor_type='partial')
        'F**k!'
    """
    ### check long words first!
    offensive_words = ["cocksucker", "motherfucker",
                       "shit", "piss", "fuck", "cunt", "tits"]
    censored_text = text
    
    for word in offensive_words:
        if censor_type == 'full':
            censored_text = re.sub(rf'\b{word}\b', '*'*len(word), censored_text, 
                                   flags=re.IGNORECASE)
        elif censor_type == 'partial':
            print(word)
            m = re.search(rf'\b({word})\b', censored_text, flags=re.IGNORECASE)
            if m:
              matched=m.group(0)
              censored_text = re.sub(rf'\b{matched}\b', 
                                     matched[0] + '*'*len(matched[1:-1]) + matched[-1],
                                     censored_text) 
        elif censor_type == 'bleep':
            if  len(word) > 4:
                censored_text = re.sub(rf'\b{word}\b', 'bleepbleep', 
                                       censored_text, flags=re.IGNORECASE)
            else:
                censored_text = re.sub(rf'\b{word}\b', 'bleep', 
                                       censored_text, flags=re.IGNORECASE)
    return censored_text



text = """안녕 (annyeong) = hi/bye (informal)
안녕하세요 (annyeonghaseyo) = hello (polite)
안녕하십니까 (anyeonghasimnikka) = hello (formal)
만나서 반갑습니다 (mannaseo bangapseumnida) = nice to meet you
저 (jeo) = I, me
제 (je) = my = 저의
제 = my 
"""

def process_line(line):
    """
    Processes a line of text containing Korean, transliteration, and English meanings.
    Returns:
        dict: Parsed information including 'ko' (Korean), 'tr' (transliteration), 'en' (English meanings), and 'meta' (metadata if available).
        
    Example:
        >>> process_line("안녕하세요 (annyeonghaseyo) = hello (polite)")
        {'ko': '안녕하세요', 'tr': 'annyeonghaseyo', 'en': ['hello'], 'meta': 'polite'}
        >>> process_line("저 (jeo) = I, me")
        {'ko': '저', 'tr': 'jeo', 'en': ['I', 'me']}
    """
    data = dict()

    p1 = re.compile(r'^([^(]+)\s+\(([^)]+)\)\s+=\s+(.*)')
    m1 = p1.match(line)
    if m1:
        data['ko'] = m1.group(1)
        data['tr'] = m1.group(2)
        rhs = m1.group(3) #rhs
    else:
        p2 = re.compile(r'^([^(]+)\s+=\s+(.*)')
        m2 = p2.match(line)        
        if m2:
            data['ko'] = m2.group(1)
            rhs = m2.group(2)

    en, meta =  process_rhs(rhs)
    if en:
        data['en'] = en
    if meta:
        data['meta'] = meta
    return data

def process_rhs(line):
    """
    Processes the right-hand side of a line to extract English meanings and metadata if available.
    
    Returns:
        tuple: A tuple containing a list of English meanings and a metadata string.
        
    Example:
        >>> process_rhs("hello (polite)")
        (['hello'], 'polite')
        >>> process_rhs("nice to meet you")
        (['nice to meet you'], '')
    """
    data = dict()

    p1 = re.compile(r'^(.*)\s+\((.*)\)')
    m1 = p1.match(line.strip())
    if m1:
        ens = m1.group(1)
        meta = m1.group(2)
    else:
        ens, meta = line, ''
    en = []
    for e in ens.split(', '):
        for ee in e.split('/'):
            en.append(ee)
        
    return en, meta


for l in text.split('\n'):
    if not l.strip():  #ignore blank lines
        continue
    data = process_line(l.strip())
    print(data)





if __name__ == "__main__":
     import doctest
     doctest.testmod(verbose=True) # normally use default verbose=False
