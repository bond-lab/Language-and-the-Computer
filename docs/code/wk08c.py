import re


def get_trans(text):
    # Define the pattern for book titles in their original language with Chinese translations
    pattern = r'《([^》]+)》\s*\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

text = "我最近读了一本书《Pride and Prejudice》 (傲慢与偏见)，还有《Les Misérables》 (悲惨世界)。"


print('Input:', text)
print(get_trans(text))



def extract_repeated_onomatopoeia(text):
    # Define the pattern for repeated onomatopoeia (e.g., ピカピカ, ドキドキ)
    pattern = r'([\u30a0-\u30ff]{2})\1'
    matches = re.findall(pattern, text)
    # Reconstruct the full onomatopoeia words from the matches
    return [match * 2 for match in matches]

text = "空がピカピカ光っていたし、心臓がドキドキしていました。彼はニコニコ笑っていました。"

print('Input:', text)
print(extract_repeated_onomatopoeia(text))

import urllib.request
response = urllib.request.urlopen('https://bond-lab.github.io/Language-and-the-Computer/code/duowiki/vocab-Japanese.txt')

text = response.read().decode('utf-8')

print('Input: Japanese duowiki')
print(extract_repeated_onomatopoeia(text))



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # normally use default verbose=False
