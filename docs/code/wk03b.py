person = ('Fred', 12)
(name, age) = person
if age < 2:
    print(f"{name} is a baby. Sleep Well!")
elif age < 4:
    print(f"{name} is a toddler. Be Cute!")
elif age < 8:
    print(f"{name} is an infant. Enjoy Life!")
elif age < 13:
    print(f"{name} is a child.  Learn Stuff!")
elif age < 20:
    print(f"{name} is a teenager. Have Fun!")
else:
    print(f"{name} is an adult. Work Hard!")



print("\nCzech morphology 😱")

čislo = ["jeden", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset"]

for n in čislo:
    if  n == "jeden":
        teen= "jedenáct"
    elif n ==  "čtyři":
        teen =  "čtrnáct"
    elif n == 'pět':
        teen = 'patnáct'
    elif n == 'devět':
        teen =   "devatenáct"   
    elif n == 'deset':
        teen =  "dvacet" # not really a teen anymore
    else:
        teen = n + 'náct'
    print(f"{n} - {teen}") 


