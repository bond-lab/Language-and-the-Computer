import nltk 

print ("\nRegular Expressions\n")

print ("[a-zA-Z]+")
print ("matches one or more ascii letters")
print ("[A-Z][a-z]*")
print ("matches zero or more ascii letters")
print ("p[aeiou]{,2}t")
print ("matches p followed by up to 2 vowels, followed by t")
print ("\\d+(\\.\\d+)?")
print ("matches a digit followed possibly by a full stop and more digits")
print ("([^aeiou][aeiou][^aeiou])*")
print ("Matches zero or more CVC combinations")
print ("\\w+|[^\\w\\s]+")
print ("Matches one or more letters or one or more (non (letters or white space))")

##    Test your answers using nltk.re_show().

print ("\nStrings and things\n")

## Define a string raw containing a sentence of your own choosing. Now, split raw on some character other than space, such as 's'.

raw = "Peter piper picked a peck of pickled peppers"
print (raw.split('p'))

# Write a for loop to print out the characters of a string, one per line.
string = 'peter'
for i in range(len(string)):
    print (string[i])
# or
for c in string:
    print (c)

# What is the difference between calling split on a string with no argument or with ' ' as the argument, e.g. sent.split() versus sent.split(' ')? What happens when the string being split contains tab characters, consecutive space characters, or a sequence of tabs and spaces? (In IDLE you will need to use '\t' to enter a tab character.)
raw = "Peter piper picked\n a peck  of pickled peppers"
print
print (raw.split())
print (raw.split(' '))
##
## split's default is \s+ so it groups whitespace together
##

# Create a variable words containing a list of words. Experiment with words.sort() and sorted(words). What is the difference? 

words = raw.split()
print
print (sorted(words))
print (words)
print (words.sort())
print (words)
