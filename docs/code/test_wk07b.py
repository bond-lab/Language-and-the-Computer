import pytest
from wk07b import analyze_text, swear_filter

def test_analyze_text_czech():
    assert analyze_text("Žlutý kůň skáče") == {
        'total': 13,
        'ascii': 7, 'accented': 6 ,
        'vowels': 4, 'consonants': 9
    }

def test_analyze_text_pinyin():
    assert analyze_text("Zhōngguó") == {
        'total': 8,
        'ascii': 6, 'accented': 2,
        'vowels': 3, 'consonants': 5
    }

def test_analyze_text_vietnamese():
    assert analyze_text("không có lỗi ở đây") == {
        'total': 14,
        'ascii': 8, 'accented': 6,
        'vowels': 6, 'consonants': 8
    }



def test_swear_filter_full():
    assert swear_filter("You are a shit and a fuck") == \
        "You are a **** and a ****"

def test_swear_filter_partial():
    assert swear_filter("You are a shit and a fuck",
                        censor_type='partial') == \
        "You are a s**t and a f**k"

def test_swear_filter_bleep():
    assert swear_filter("You are a shit and a cocksucker",
                        censor_type='bleep') == \
        "You are a bleep and a bleepbleep"


@pytest.mark.xfail(reason="we don't know regular expressions")
def test_swear_filter_in_words():
    # This is a known issue test that highlights the need to avoid censoring within words.
    # Should pass without censorship 
    assert swear_filter("People in Scunthorpe like petits fours with shittake mushrooms") == \
        "People in Scunthorpe like petits fours with shittake mushrooms"  
