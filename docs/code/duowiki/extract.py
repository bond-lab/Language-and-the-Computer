from bs4 import BeautifulSoup
import urllib.request
import time

def text_from_url(url):
    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')

def extract_vocabulary(html):
    #with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(html, 'html.parser')
    
    # Assuming vocabulary sections are identifiable by specific tags or headings
    # This may vary depending on the structure of the file
    lessons = soup.find_all(['h3', 'li'])  # adjust tags as needed
    vocabulary_text = []

    current_lesson = ""
    for element in lessons:
        if element.name in ['h3']:
            # New lesson section
            current_lesson = element.get_text().strip()
            if "lesson" in current_lesson.lower():
                vocabulary_text.append(f"\n{current_lesson}\n")
            #print('CL', current_lesson)
        elif element.name == 'li':
            # Extract paragraph text that might contain vocabulary items
            text = element.get_text().strip()
            if "=" in text.lower():
                vocabulary_text.append(text)

    # Join list into a single text block and return
    return "\n".join(vocabulary_text)

def get_skills(lang):
    """
    Extract a list of skills for a given language
    """
    wikiroot = 'https://duolingo.fandom.com'
    langtext = text_from_url(f"{wikiroot}/wiki/{lang}")
    skillroot = f'/wiki/{lang}_Skill:'
    skills = []
    for s in langtext.split('"'):
        if s.startswith(skillroot):
            skill = s[len(skillroot):]
            skills.append((skill, f'{wikiroot}{s}'))
    return skills



langs = ['Chinese', 'Japanese', 'Vietnamese', 'Indonesian', 'Korean', 'Cantonese']

for lang in langs:
    urls = get_skills(lang)
    with open(f'vocab-{lang}.txt', 'w') as out:
        print(f'# Vocabulary for {lang}',
              file = out)
        for i, (title, url) in enumerate(urls):
            print(f'Processing {lang}: {title} ({i})')
            html = text_from_url(url)
            vocab_text = f"\n=== Skill {i} - {title} ===\n\n" +  extract_vocabulary(html)
            print(vocab_text,
                  file=out)
            time.sleep(10)
        print(file=out)
    
#urls = []
# with open('URLs', 'r') as file:
#     for l in file:
#         urls.append(l.strip())


# for i, url in enumerate(urls):
#     html = text_from_url(url)
#     title = url[45:]
#     vocab_text = f"\n=== Skill {i} - {title} ===\n\n" +  extract_vocabulary(html)
#     time.sleep(10) 
#     print(vocab_text)
