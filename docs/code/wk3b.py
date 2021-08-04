###
### 
###
def isPal(word):
    """
    Test if a word or phrase is a palindrome (same backward or forward).

    Assume it must have more than 2 letters, and that only letters and digits count.
    """
    ### keep only letters or numbers
    w = ''.join([l for l in word.lower() if l.isalnum()])
    ### check if it is the same as its reverse
    return len(w) > 1 and w == w[::-1]   

### Test this on good AND bad input

tests = ["eve", "Eve", "Madam, I'm Adam", "Rats live on no evil star", 
         "Adam", "1", ',', "A man, a plan, a canal, panama."]

print("\nTesting Palindromes on test suite\n")
for t in tests:
    ### use the tab to line things up
    print(isPal(t), '\t', t)

###
### writing our own tests
###
def isDigit(word):
    """
    Test if a word is all digits.
    """
    ### keep only digits
    w = ''.join([l for l in word if l in '0123456789'])
    ### check if it is the same as it used to be
    return len(w) > 0 and word == w 

tests = ["eve", "Eve", "123", "R22", 
         "Adam", "1", ',', "23 23"]

print("\nTesting for digitness\n")
for t in tests:
    ### use the tab to line things up
    print (isDigit(t), '\t', t)
