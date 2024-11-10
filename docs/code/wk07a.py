# test with python -m doctest -v example.py


def IsReduplicated(word):
    """
    return True is a word is reduplicated
    ignore case
    >>> IsReduplicated("buku-buku")
    True
    >>> IsReduplicated("Buku-buku")
    True
    >>> IsReduplicated("buku")
    False
    >>> IsReduplicated("itu-buku")
    False
    """
    parts = word.split("-")
    if len(parts) == 2 and parts[0].lower() == parts[1].lower():
        return True
    else:
        return False

def find_redup(words):
    """
    count the number of reduplicate words
    >>> find_redup ([ "buku-buku", "kucing", "Agak-agak", "agak-agak" ])
    {'buku-buku': 1, 'agak-agak': 2}
    """
    redups = dict()
    for w in words:
        if IsReduplicated(w):
            redups[w.lower()] = redups.get(w.lower(), 0)  +1
    return redups


### Note hard to get the multiline text!
def strip_gutenberg(raw):
    """
    Strip off everything before the line '*** START'  ..., ' ***'
    and after the line '*** END OF THE PROJECT GUTENBERG EBOOK', ...

    >>> strip_gutenberg('The Project Gutenberg eBook of All cats are gray\\n...\\n*** START OF THE PROJECT GUTENBERG EBOOK ALL CATS ARE GRAY ***\\n_An odd story, made up of oddly assorted elements that include a man, \\n    a woman, a black cat, a treasure--and an invisible being that had to\\n  be seen to be believed._\\n*** END OF THE PROJECT GUTENBERG EBOOK ALL CATS ARE GRAY ***\\nMost people start at our website which has the main PG search\\nfacility: www.gutenberg.org.')
    '_An odd story, made up of oddly assorted elements that include a man, \\n    a woman, a black cat, a treasure--and an invisible being that had to\\n  be seen to be believed._'
    """
    ### go to the start of the start message
    start = raw.index('*** START')
    raw = raw[start:]
    ### go to the end of the start message
    start = raw.index (' ***')
    raw = raw[start + 5:]

    ### go to the start of the end message
    end = raw.index('*** END OF THE PROJECT GUTENBERG EBOOK')
    return raw[:end].strip()



def process_line(line, lesson):
    """
    Extract information from duolingo wiki
    >>> process_line('ne = no/not', 1)
    {'lesson': 1, 'cs': 'ne', 'en': ['no', 'not']}
    >>> process_line('na shledanou = goodbye/bye, see you soon', 3)
    {'lesson': 3, 'cs': 'na shledanou', 'en': ['goodbye', 'bye', 'see you soon']}
    """
    word = dict()
    cs, en = line.split(' = ')
    word['lesson'] = lesson
    word['cs'] = cs
    word['en'] = []
    for e in en.split(', '):
        for ee in e.split('/'):
            word['en'].append(ee)
    return word


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # normally use default verbose=False
