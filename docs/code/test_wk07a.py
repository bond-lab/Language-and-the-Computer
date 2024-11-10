# pytest -v test_wk07a.py

import pytest
from wk07a import IsReduplicated, find_redup, strip_gutenberg, process_line

def test_IsReduplicated():
    assert IsReduplicated("buku-buku") == True
    assert IsReduplicated("Buku-buku") == True
    assert IsReduplicated("buku") == False
    assert IsReduplicated("itu-buku") == False
    assert IsReduplicated("Kucing-kucing") == True
    assert IsReduplicated("rumah") == False

def test_find_redup():
    words = ["buku-buku", "kucing", "Agak-agak", "agak-agak", "rumah", "rumah-rumah"]
    result = find_redup(words)
    expected = {'buku-buku': 1, 'agak-agak': 2, 'rumah-rumah': 1}
    assert result == expected

def test_strip_gutenberg():
    raw_text = ("""
The Project Gutenberg eBook of All cats are gray
...
*** START OF THE PROJECT GUTENBERG EBOOK ALL CATS ARE GRAY ***
_An odd story, made up of oddly assorted elements that include a man,
a woman, a black cat, a treasure--and an invisible being that had to
be seen to be believed._
*** END OF THE PROJECT GUTENBERG EBOOK ALL CATS ARE GRAY ***\n'
Most people start at our website which has the main PG search\nfacility: www.gutenberg.org.
""")
    result = strip_gutenberg(raw_text)
    expected = ("""_An odd story, made up of oddly assorted elements that include a man,
a woman, a black cat, a treasure--and an invisible being that had to
be seen to be believed._""")
    assert result == expected

def test_process_line():
    assert process_line('ne = no/not', 1) == {'lesson': 1, 'cs': 'ne', 'en': ['no', 'not']}
    assert process_line('na shledanou = goodbye/bye, see you soon', 3) == {'lesson': 3, 'cs': 'na shledanou', 'en': ['goodbye', 'bye', 'see you soon']}
    assert process_line('dobry den = good day/hello', 2) == {'lesson': 2, 'cs': 'dobry den', 'en': ['good day', 'hello']}
