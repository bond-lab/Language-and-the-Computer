###
### Week 2: Before Class
###


# Make a list that includes at least three people you’d
# like to invite to dinner. Then use your list to print a message to
# each person, inviting them to dinner.  Try to choose interesting
# people (like in Van Loon's Lives)

guests = ["Conan Doyle", "Isaac Newton", "Dorothy Sayers"]

print(f"Welcome to dinner {guests[0]}")
print(f"Welcome to dinner {guests[1]}")
print(f"Welcome to dinner {guests[2]}")

# You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

#  Start with your program from the first exercise and add a print() call to the end of your program, informing people that you found a bigger table.

print("We have some more space, I will invite some more people.")

#  Use  insert() to add one new guest to the beginning of your list.
#  Use  insert(?) to add one new guest to the middle of your list.
#  Use  append() to add one new guest to the end of your list.

guests.insert(0, "C. J. Cherryh")
guests.insert(2, "Marie Curie")
guests.append("Oscar Wilde") 

print(guests)

# Use len() to print a message indicating the number of people you’re inviting to dinner.

print(f"I invited {len(guests)} guests")

#  Use a for loop to print a message to each of your guests, and then write a general message to all of them outside of the list

for guest in guests:
    print(f"Welcome to dinner {guest}")
print("The party is at my house, starting at 7pm sharp")

#  Do the same thing, but printing the names in alphabetical order

for guest in sorted(guests):
    print(f"Welcome to dinner {guest}")
print("The party is at my house, starting at 7pm sharp")

#  Use list comprehension,  len() and  max() to say how long the longest name is 

print(f"The longest name has length {max([len(g) for g in guests])}.")
