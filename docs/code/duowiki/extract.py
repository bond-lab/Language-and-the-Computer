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

urls = []
with open('URLs', 'r') as file:
    for l in file:
        urls.append(l.strip())


for i, url in enumerate(urls):
    html = text_from_url(url)
    title = url[45:]
    vocab_text = f"\n=== Skill {i} - {title} ===\n\n" +  extract_vocabulary(html)
    time.sleep(10) 
    print(vocab_text)
