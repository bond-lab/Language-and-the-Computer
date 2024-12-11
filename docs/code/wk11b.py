###
### Plot cubes from 1 to 1,000
###

import matplotlib.pyplot as plt
import tuftelike

udhr = {"en": {"ADJ": 158, "ADV": 27, "NOUN": 443, "VERB": 139, "PROPN": 31, "INTJ": 0, "ADP": 246, "AUX": 90, "CCONJ": 129, "SCONJ": 15, "DET": 178, "NUM": 29, "PART": 42, "PRON": 85, "PUNCT": 154, "SYM": 0, "X": 0}, "cs": {"ADJ": 214, "ADV": 36, "NOUN": 434, "VERB": 114, "PROPN": 1, "INTJ": 0, "ADP": 133, "AUX": 58, "CCONJ": 121, "SCONJ": 31, "DET": 113, "NUM": 26, "PART": 5, "PRON": 41, "PUNCT": 173, "SYM": 0, "X": 0}, "id": {"ADJ": 103, "ADV": 48, "NOUN": 439, "VERB": 187, "PROPN": 23, "INTJ": 0, "ADP": 174, "AUX": 1, "CCONJ": 114, "SCONJ": 16, "DET": 70, "NUM": 27, "PART": 27, "PRON": 69, "PUNCT": 135, "SYM": 0, "X": 0}, "zh": {"ADJ": 47, "ADV": 174, "NOUN": 776, "VERB": 825, "PROPN": 35, "INTJ": 0, "ADP": 140, "AUX": 0, "CCONJ": 115, "SCONJ": 0, "DET": 75, "NUM": 208, "PART": 232, "PRON": 46, "PUNCT": 200, "SYM": 0, "X": 5}, "ko": {"ADJ": 70, "ADV": 131, "NOUN": 417, "VERB": 166, "PROPN": 4, "INTJ": 0, "ADP": 0, "AUX": 10, "CCONJ": 116, "SCONJ": 54, "DET": 17, "NUM": 25, "PART": 0, "PRON": 2, "PUNCT": 118, "SYM": 0, "X": 0}, "ja": {"ADJ": 58, "ADV": 6, "NOUN": 671, "VERB": 229, "PROPN": 8, "INTJ": 0, "ADP": 458, "AUX": 184, "CCONJ": 75, "SCONJ": 70, "DET": 18, "NUM": 36, "PART": 25, "PRON": 7, "PUNCT": 212, "SYM": 0, "X": 0}, "vi": {"ADJ": 78, "ADV": 0, "NOUN": 428, "VERB": 275, "PROPN": 58, "INTJ": 0, "ADP": 107, "AUX": 9, "CCONJ": 34, "SCONJ": 50, "DET": 67, "NUM": 50, "PART": 2, "PRON": 0, "PUNCT": 133, "SYM": 0, "X": 90}}

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()

upos   = list(udhr['en'].keys())
endist = list(udhr['en'].values())

ax.bar(upos, endist)

ax.set_xlabel("Part of Speech")  # Add a x-label to the axes.
ax.set_ylabel("Frequency")  # Add a y-label to the axes.
ax.set_title("UDHR (en)")  # Add a title to the axes.
plt.xticks(rotation=45, ha='right') # rotate the axis labels (I googled for this)

plt.savefig("wk11b-fig1.png")
#plt.show()
plt.close()

### do all the languages


upos   = list(udhr['en'].keys())

for lang in udhr:
    plt.style.use('seaborn-v0_8-dark-palette')
    fig, ax = plt.subplots()
    ax.bar(upos, list(udhr[lang].values()), label=lang)
    ax.bar('ADJ', udhr[lang]['ADJ'], color='green')
    ax.bar('VERB', udhr[lang]['VERB'], color='lightgreen')
    ax.set_xlabel("Part of Speech")  # Add a x-label to the axes.
    ax.set_ylabel("Frequency")  # Add a y-label to the axes.
    ax.set_title(f"UDHR {lang}")  # Add a title to the axes.
    plt.xticks(rotation=45, ha='right') # rotate the axis labels (I googled for this)
    plt.savefig(f"wk11b-fig2-{lang}.png")
    plt.close()
    #plt.show()


    
for lang in udhr:
    plt.style.use('seaborn-v0_8-dark-palette')
    fig, ax = plt.subplots()
    ax.set_ylim(0, 900)
    ax.set_yticks = range(0, 900, 100)
    ax.bar(upos, list(udhr[lang].values()), label=lang)
    ax.bar('ADJ', udhr[lang]['ADJ'], color='green')
    ax.bar('VERB', udhr[lang]['VERB'], color='lightgreen')
    ax.set_xlabel("Part of Speech")  # Add a x-label to the axes.
    ax.set_ylabel("Frequency")  # Add a y-label to the axes.
    ax.set_title(f"UDHR {lang}")  # Add a title to the axes.
    plt.xticks(rotation=45, ha='right') # rotate the axis labels (I googled for this)
    plt.savefig(f"wk11b-fig3-{lang}.png")
    plt.close()
    #plt.show()
