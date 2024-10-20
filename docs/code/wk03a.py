# Things that evaluate to True and False

print(f"1+1 == 2 is {1+1 == 2}")
print(f"'IT'.lower() == 'it'  is {'IT'.lower() == 'it'}")
print('...')
print(f"1+1 ! 2 is {1+1 != 2}")
print(f"'IT'.title() == 'it' is {'IT'.title() == 'it'}")
print('...')
print(f"3 in range(0,3) is {3 in range(0,3)}")
print(f"3 in range(0,4) is {3 in range(0,4)}")
print()

print('\nStages of life')

age=42

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 8:
    print("The person is an infant.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
else:
    print("The person is an adult.")
