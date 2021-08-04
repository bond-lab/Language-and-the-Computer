###
### Practical work (week 6)
###

##
## Take the following Chinese verbs ['学习', '开'] and 
## write code to produce the following variants:
## ['学习学习', '开开'] # reduplication
## ['学习不学习',　'学不学习',　'开不开'] # yes-no questions 
## 
print ("\n")
verbs = ['学习', '开'] 
print("Verbs", verbs)
verbsverbs= [w+w for w in verbs]
print("Reduplicated verbs", verbsverbs)
verbsnotverbs= []
for v in verbs:
    if len(v) ==2:
        verbsnotverbs.append('{}不{}'.format(v[0],v))
    verbsnotverbs.append('{0}不{0}'.format(v))
print("Verb or not?", verbsnotverbs)

print ("\n")
print("You can manipulate it even if you can't read it!\n")
print ("\n\n")
#In honour of Michael Palin, define a function isPalin(string) that
#decides whether string is a palindrome. This should be a Boolean
#function, it returns True if string is a palindrome or False if it is
#not.

def isPalin(string):
    '''Return true if string is a palindrome'''
    return string == string[::-1]


# Write code to test the function with strings like "spam maps",
# "Palin Drome". The tests should output the results, like this:
#          "spam maps" is a palindrome.
#          "Palin Drome" is not a palindrome.

for s in ["spam maps", "Palin Drome"]:
    if isPalin(s):
        print ('"{}" is a palindrome.'.format(s))
    else:
        print ('"{}" is not a palindrome.'.format(s))

# Note that the test result messages are output by the test code, 
# not by the function. The function only returns True or False.

# Define a non-Boolean function normalize(string) that takes a string
# argument and returns a new string with all punctuation and
# whitespace removed and all uppercase letters changed to lowercase
# letters.

def normalize(string):
    '''return a new string with all punctuation and whitespace removed and all letters downcased'''
    return ''.join(c.lower() for c in string if c.isalnum())


 #    Test this function with strings like "Spam! Maps!", "Palin? Drome?". The tests should output messages, like this:

 #    "Spam! Maps!" normalized to "spammaps".
 #    "Palin? Drome?" normalized to "palindrome".

print ("\n\n")

for s in ["spam maps", "Palin Drome", "Spam! Maps!", "Palin? Drome?"]:
    print ('"{}" normalized to "{}".'.format(s, normalize(s)))

 #    Define a Boolean function isPalinNormal(string) that decides whether string is a palindrome, disregarding upper/lowercase, punctuation and whitespace. Use both normalize() and isPalin() inside isPalinNormal().

def isPalinNormal(string):
    '''Return true if normalized string is a palindrome'''
    return isPalin(normalize(string))

 #    Test this function with strings like "Spam! Maps!", "Palin? Drome?". The tests should output messages, like this:

 #    "Spam! Maps!" is a palindrome when normalized.
 #    "Palin? Drome?" is not a palindrome when normalized.

print ("\n\n")

for s in ["spam maps", "Palin Drome", "Spam! Maps!", "Palin? Drome?"]:
    if isPalin(s):
        print ('"{}" is a palindrome'.format(s))
    elif isPalinNormal(s):
        print ('"{}" is a palindrome when normalized.'.format(s))
    else:
        print ('"{}" is not a palindrome under any circumstances.'.format(s))


###
### Test (general test of the functions) 
###

print("\nWith a test harness\n")

test = dict()
test["madam"] = True
test["eve"] = True
test["adam"] = False
test["Madam I'm Adam"] = True
test['1 on 1'] = False
test['1 ono 1'] = True
test["This isn't"] = False
test["Neither is this"] = False
for s in test:
    #print "Do I think", string, "is a palindrome:", isPalin(string), "(", isPalin(string) == test[string], ")"
    print ('Do I think normalized "{}" is a palindrome? {}\n\t(Test OK: {})'.format(s,
                                                                                 isPalinNormal(s), isPalinNormal(s) == test[s]))




