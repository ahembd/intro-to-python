# Create a variable called number. Set it to any integer.
# If the number is divisible by 3, print 'Fizz'
# If the number is divisible by 5, print 'Buzz'
# If the number is divisible by both 3 and 5, print 'FizzBuzz'
num = int(input('Enter a number:'))
if num % 3 == 0 and not(num % 5 == 0):
    print('Fizz')
elif num % 5 == 0 and not num % 3 == 0:
    print('Buzz')
elif num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')

