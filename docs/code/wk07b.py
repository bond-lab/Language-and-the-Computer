def analyze_text(text):
    """
    Analyzes a text to count characters, ASCII characters, accented characters,
    vowels, and consonants.
    Returns:
        dict: A dictionary containing counts of characters by type.
        
    Example:
        >>> analyze_text("Hà Nội có mưa")
        {'total': 10, 'ascii': 6, 'accented': 4, 'vowels': 6, 'consonants': 4}
        >>> analyze_text("pīnyīn")
        {'total': 6, 'ascii': 4, 'accented': 2, 'vowels': 2, 'consonants': 4}
    """
    result = {
        'total': len([t for t in text if t.isalpha()]),
        'ascii': 0,
        'accented': 0,
        'vowels': 0,
        'consonants': 0,
    }
    
    vowels = "aeiouáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõōọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ"
    # combining
    vowels += 'āēê̄īōūǖĀĒÊ̄ĪŌŪǕáéếíóúǘÁÉẾÍÓÚǗǎěê̌ǐǒǔǚǍĚÊ̌ǏǑǓǙàèềìòùǜÀÈỀÌÒÙǛaeêiouüAEÊIOUÜ'
    vowels = vowels + vowels.upper()
    
    for char in text:
        if char.isalpha():
            if char.isascii():
                result['ascii'] += 1
            else:
                result['accented'] += 1
            if char in vowels:
                result['vowels'] += 1
            else:
                result['consonants'] += 1

    return result

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
    """
    ### check long words first!
    offensive_words = ["cocksucker", "motherfucker",
                       "shit", "piss", "fuck", "cunt", "tits"]
    censored_text = text
    
    for word in offensive_words:
        if censor_type == 'full':
            censored_text = censored_text.replace(word,
                                                  '*' * len(word))
        elif censor_type == 'partial':
            censored_text = censored_text.replace(word,
                                                  word[0] + '*' * (len(word) - 2) + word[-1])
        elif censor_type == 'bleep':
            if  len(word) > 4:
                censored_text = censored_text.replace(word, 'bleepbleep')
            else:
                censored_text = censored_text.replace(word, 'bleep')
    
    return censored_text









if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # normally use default verbose=False
