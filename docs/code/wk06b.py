import toml, yaml, json

with open("duowiki/skill0.txt") as f:
    duo = f.read()

lesson = ''

def process_line(line, lesson):
    word = dict()
    cs, en = line.split(' = ')
    word['lesson'] = lesson
    word['cs'] = cs
    word['en'] = []
    for e in en.split(', '):
        for ee in e.split('/'):
            word['en'].append(ee)
    return word

def process_duo(duo):
    lesson = ''
    exps = []
    for l in duo.splitlines():
        if l.startswith('==='):
            continue
        elif l.startswith('Lesson'):
            lesson = l.strip()[7:-2]
        elif '=' in l:
            #print(l)
            exps.append(process_line(l.strip(),
                                            lesson))
    return exps

expressions = process_duo(duo)
print (json.dumps(expressions,
                  indent = 2,
                  ensure_ascii = False))

stats = dict()
stats['cs']  = []
stats['en']  = []
stats['cs-en'] = []
  
for word in expressions:
    stats['cs'].append(word['cs'])
    for en in word['en']:
        stats['en'].append(en)
        stats['cs-en'].append((word['cs'], en)) 

print('\nFreq\tWord')    
for key, val in stats.items():
    print(len(val), key, sep='\t')


for word in expressions:
    match = False
    while not match:
        guess=input(f"""What is an English translation of {word['cs']}
 (or q to quit)? """)
        if guess == 'q':
            break
        elif guess in word['en']:
            print('Well done!')
            match = True
