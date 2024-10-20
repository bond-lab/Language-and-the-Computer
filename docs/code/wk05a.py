
print("\nFirst function:\n")

def pizza(flavour, size):
    """
    pretend to make a pizza
    """
    print (f"We will make a {size} {flavour} pizza")

pizza('diavola', 'small')
pizza('quatro formaggio', size='large')
pizza(size='family-size', flavour='artichoke')

print("\n\nSecond function (with defaults):\n")

def pizza(flavour='pepperoni', size='large'):
    """
    pretend to make a pizza
    default to a large pepperoni
    """
    print (f"We will make a {size} {flavour} pizza")

pizza()    
pizza('diavola', 'small')
pizza('quatro formaggio')
pizza(size='family-size', flavour='artichoke')

print("\n\nThird function (with averages):\n")

def average(numbers):
  """ 
  Return the average of a list of numbers
  """
  total = sum(numbers)       # Calculate the sum of the numbers
  count = len(numbers)       # Find the length (number of items in the list)
  return   total / count    # Calculate the average


my_numbers = [10, 20, 30, 40, 50]
print(f"The average of {my_numbers} is {average(my_numbers)}")


print("\n\nFourth function (with averages and check for []):\n")

def average(numbers):
  """ 
  Return the average of a list of numbers
  or None if the list is empty
  """
  if numbers:
    total = sum(numbers)       # Calculate the sum of the numbers
    count = len(numbers)       # Find the length (number of items in the list)
    return   total / count    # Calculate the average
  else:
    print ("The list is empty!")
    return None

print(f"The average of {my_numbers} is {average(my_numbers)}")

print(f"The average of {[]} is {average([])}")

print("\n\nFifth function same as the fourth:\n")
### normally do this at the top of the file
from mymath import average as av

print(f"The average of {my_numbers} is {av(my_numbers)}")

print(f"The average of {[]} is {av([])}")

print("\n\nSixth function (built in):\n")
### normally do this at the top of the file
from statistics import mean as av

print(f"The average of {my_numbers} is {av(my_numbers)}")


