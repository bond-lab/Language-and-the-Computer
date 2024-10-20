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
    print ("The list is empty")
    return None


