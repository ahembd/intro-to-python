# You're creating a program to determine eligibility for a discount. Here's what you need to do:
# Take user's age and income as input:

age = int(input('Enter your age: '))
income = int(input('Enter your monthly income: '))

# Now, apply the follow45ing conditions and print messages accordingly:
if age >= 18 and income <= 1000:
    print ('You qualify for the discount!')
elif age < 18 or income == 0:
    print ('You get a special discount!')
else:
    print ('Sorry, you are not eligible for any discount.')

# Remember to use the and, or operators to combine conditions as needed.
