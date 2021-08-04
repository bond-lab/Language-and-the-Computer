###
### Week 2:  Before Class
###

## Make a list of the words one two three o'clock four o'clock rock
words = ["one", "two", "three", "o'clock", "four", "o'clock",  'rock']

##   Pick out the first word as a string
words[0]

## Pick out the first word as a list
words[0:1]

##    Pick out the last word as a string
words[-1]

##    Show how many words there are in the list
len(words)

##    Transform the list into a new list that only has numbers in it
##    take as many steps as you need
[len(w) for w in words]

##    Count how many times o'clock appears in the list 
words.count("o'clock")

print("No output for this")
