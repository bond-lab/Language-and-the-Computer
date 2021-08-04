for i in range(1,10,2):
      print ("i = ", i)

i = 1
while (i <=10):
    print ("i = ", i)
    i +=2
print()

i = 20
while (i > 0):
      print ("i = ", i)
      i -= 1

for i in range(20,0,-1):
      print ("i = ", i)
print()

for x in [-1, (), {}, 0, None, '', ' ', (0), {0:0}, 'False', False]:
    print("'{}' evaluates to {}".format(x, bool(x)))
