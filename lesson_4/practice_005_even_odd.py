# Create a variable called number. Set it to any number.

# Using if else statement, create the logic that will print "Even" for even numbers or "Odd" for odd numbers.

# Odd numbers are: 1, 3, 5, 7, etc.
# Even: 2, 4, 6, etc.
num = int(input('Enter a number:'))
if num % 2 == 0:
    print('This number is even.')
else:
    print('This number is odd.')