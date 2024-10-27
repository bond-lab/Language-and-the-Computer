###
### we will use this to get text from the web
###
import urllib.request
import json, yaml, toml

def text_from_url(url):
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print(f"I couldn't find: {url}")
    else:
        return response.read().decode('utf-8')

### read from Gutenberg

raw = text_from_url("https://www.gutenberg.org/cache/epub/29019/pg29019.txt")

## save

with open("acag-raw.txt", 'w') as f:
    f.write(raw)

## read

with open("acag-raw.txt") as f:
    raw = f.read()

### save just the story

story = raw[1650: -19030]

with open("acag.txt", 'w') as f:
    f.write(story)

stats = dict()

stats['Characters'] = len(story)
stats['Lines'] = len(story.splitlines())
### approximations
stats['Words'] = len(story.split()) 
stats['Sentences'] = story.count('.') + story.count('!') + story.count('?')  

with open('stats.yaml', 'w') as outfile:
    yaml.dump(stats, outfile)

with open('stats.json', 'w') as outfile:
    json.dump(stats, outfile)

with open('stats.toml', 'w') as outfile:
    toml.dump(stats, outfile)

raw = text_from_url("https://www.gutenberg.org/cache/epub/29019/pg29019a.txt")

def strip_gutenberg(raw):
    """
    Strip off everything before the line '*** START'  ..., ' ***'
    and after the line '*** END OF THE PROJECT GUTENBERG EBOOK', ...
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

raw = text_from_url("https://www.gutenberg.org/cache/epub/2852/pg2852.txt")

cooked = strip_gutenberg(raw)

print('\n*** The beginning\n')
print(cooked[:200])

print('\n*** The end\n')
print(cooked[-200:])
