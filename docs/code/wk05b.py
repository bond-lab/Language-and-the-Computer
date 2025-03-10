print("\n\nPrint list\n")

def print_items(*items):
    """
    print each item on a new line
    """
    for item in items:
        print(item)

# Example call
print_items("apple", "banana", "cherry")

print("\n\nPrint details\n")

####

def print_details(**details):
    """
    print the details, formatted nicely
    """
    for key, value in details.items():
        print(f"{key}: {value}")

# Example call
print_details(name="Alice", age=25, city="Olomouc")

print("\n\nReduplication\n")

def IsReduplicated(word):
    """
    return True is a word is reduplicated
    ignore case
    """
    parts = word.split("-")
    if len(parts) == 2 and parts[0].lower() == parts[1].lower():
        return True
    else:
        return False

# Example calls
for word in ["buku-buku", "rumah"]:
    print(f"{word}: {IsReduplicated(word)}")


print("\n\nFind Reduplication\n")
    
def find_redup(words):
    redups = dict()
    for w in words:
        if IsReduplicated(w):
            redups[w.lower()] = redups.get(w.lower(), 0)  +1
    return redups


# from https://arqu3fiq.blogspot.com/2007/12/kumo-no-ito.html

text = """Ini adalah Chi no Ike  di dasar Neraka , tempat 
timbul-tenggelamnya Kandata bersama para pendosa lain . Dilihat 
dari sudut manapun tempat ini gelap pekat . Terkadang , dari balik 
kegelapan , samar-samar terlihat kilauan jaru-jarum dari Bukit 
Jarum yang mengerikan . Kengerian yang muncul tidak terperikan . 
Ditambah lagi suasananya yang senyap bagai dalam kuburan , 
seringali sayup-sayup hanya terdengar suara lenguhan nafas 
para pendosa . Orang-orang yang samapi jatuh ke tempat ini , 
begitu kelelahan oleh berbagai macam siksaan Neraka sampai-sampai 
tidak lagi punya tenaga untuk mengeluarkan rintihan derita . 
Karenanya , tentu sajasi maling besar Kandata pun sesenggukan 
di kubangan darah dalam kolam dan gelagapan persis seperti 
katak sekarat yang tidak bisa berbuat apa-apa ."""


redups=find_redup(text.split())
print(redups) 


print("\n\nInformal\n")

def informal (words):
    infrml = []
    for word in words:
        if IsReduplicated(word):
            ### change to non-reduplicated version
            word = word.split('-')[0] + '2'
        infrml.append(word)
    return infrml

informal_text = informal(text.split())
print(informal_text)


