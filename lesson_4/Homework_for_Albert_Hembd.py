# Homework Lesson 4 - Conditionals

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 1: Temperature Classification
# You're developing a weather application. Write a program that takes 
# a temperature in Fahrenheit as input. If the temperature is above 
# 85°F, print "Hot day ahead!".
temperature = int(input("Enter the temperature in Fahrenheit: "))
if temperature > 85:
    print('Hot day ahead!')
elif 65 <= temperature < 85:
    print('It will be a pleasant day today.')
elif temperature < 65:
    print('It will be a bit cool today.')
# <Your  code here>

# ---------------------------------------------------------------------
# Exercise 2: Grade Classifier
# As a teacher, you want to automate grading. Write a program that
# takes a student's score as input and prints "Pass" if the score is
# 50 or above, otherwise print "Fail".
# Do not forget that the input() function returns a string value and
# you need to convert it so you can use the value as a number.

# <Your code here>
grade = int(input('Please enter your grade.'))
if grade > 50:
    print('Pass')
else:
    print('Fail')

# ---------------------------------------------------------------------
# Exercise 3: Scholarship Eligibility
# Your university offers scholarships based on academic performance.
# Write a program that takes a student's GPA as input. If the GPA
# is greater than or equal to 3.5, print
# "Congratulations, you're eligible for a scholarship!". If it's
# between 3.0 and 3.49, print "You're on the waiting list."
# Otherwise, print "Keep up the good work."
# Do not forget that the input() function returns a string value and
# you need to convert it so you can use the value as a number.
# The function int() converts the number to an integer, and the function
# float() converts the number to a float.

gpa = float(input("Enter your GPA: "))
if gpa > 3.5:
    print('Congratulations, you\'re eligible for a scholarship!')
elif 3.0 >= gpa <= 3.49:
    print('You\'re on the mailing list.')
else:
    print('Keep up the good work.')

# <Your code here>

# ---------------------------------------------------------------------
# Exercise 4: Shopping Discount
# A store is offering a discount on a product. Write a program that
# takes the original price and the discount percentage as input.
# If the discounted price is less than $50, print "Great deal!".
# Otherwise, print "Might want to wait for a better offer."
original_price = float(input("Enter product original price: "))
discount_percentage = float(input("Enter discount percentage: "))

discounted_price = original_price - (.01 * discount_percentage * original_price)

# <Your code here>
print('Discounted price equals: ' + str(discounted_price))
# ---------------------------------------------------------------------
# Exercise 5: Movie Night Decision
# You and your friends are deciding on a movie to watch. Write a
# program that takes two movie ratings as input. If both ratings
# are above 7, print "Let's watch both!". Otherwise,
# print "Let's just pick one."

# <Your code here>
print('Deciding what movie to watch...')

movie_1 = 'First movie'
movie_2 = 'Second movie'

def movie_rankings(movie_to_rank):
    rank = input("How do you rank this movie? Awful, Bad, Poor, Fair, OK, 'Good' or 'Excellent'")
    rating = 0

    if rank == 'Awful':
        rating = 0
    if rank == 'Bad':
        rating = 2
    if rank == 'Poor':
        rating = 4
    if rank == 'Fair':
        rating = 6
    if rank == 'OK':
        rating = 7
    if rank == 'Good':
        rating = 8
    if rank == 'Excellent':
        rating = 10
    return rating

movie_1_rating = movie_rankings('movie_1')
movie_2_rating = movie_rankings('movie_2')

if movie_1_rating >= 7:
    print('Let\'s watch both.')
else:
    print('Let\'s just watch one.')

# ---------------------------------------------------------------------
# Exercise 6: Restaurant Recommendation
# You're building a restaurant recommendation system. Write a program
# that takes a person's mood (happy or sad) and hunger level
# (high or low) as input. If they're happy and hungry, recommend
# a fancy restaurant. If they're sad and hungry, recommend comfort food.
# For other cases, recommend a casual dining place.

# <Your code here>
mood = input('Are you happy or sad?')
hunger = input('Are you hungry? Yes or No')

if mood.upper() == 'HAPPY' and hunger == 'Yes':
    print('Go to a fancy restaurant.')
elif mood.upper == 'SAD' and hunger == 'Yes':
    print('Order some comfort food.')

# ---------------------------------------------------------------------
# Exercise 7: Exercise 7: Tax Bracket Calculator
# You're building a tax calculation system. Write a program that
# takes a person's annual income as input. Use conditionals
# to determine their tax bracket based on the following rules:

# - If income is less than $40,000, tax rate is 10%.
# - If income is between $40,000 and $100,000 (inclusive), tax rate is 20%.
# - If income is greater than $100,000, tax rate is 30%.

# Remember that a tax rate of 10% can be represented as 10/100 or 0.1

# Print the calculated tax amount for the given income.
print('Figuring your taxes...')
tax_amount = 0
annual_income = float(input("Enter your annual income: "))
if annual_income <= 40000:
    print('Your tax rate is ten percent.')
    tax_amount = .1 * annual_income
elif 40000 <= annual_income < 100000:
    tax_amount = .2 * annual_income
    print('Your tax rate is twenty percent.')
elif annual_income > 100000:
    print('Your tax rate is thirty percent.')
    tax_amount = .3 * annual_income

# <Your code here>

# Print tax amount
print(f"Your tax amount is ${tax_amount}")

# ---------------------------------------------------------------------
# Exercise 8: Ticket Pricing System
# You're working on a ticket booking system for an amusement park.
# Write a program that takes a person's age as input and determines
# their ticket price based on the following rules:
# - Children (ages 3 to 12): $10
# - Adults (ages 13 to 64): $20
# - Seniors (ages 65 and above): $15
# Print the calculated ticket price for the given age.

# <Your code here>

child_ticket = 10.00
adult_ticket = 20.00
senior_ticket = 15.00
ticket_price = 0

age = int(input('What is your age?'))
if 3 <= age <= 12:
    ticket_price = child_ticket
elif 13 <= age <= 64:
    ticket_price = adult_ticket
elif age > 64:
    ticket_price = senior_ticket

print(f'The price of your ticket will be: {ticket_price}')

# ---------------------------------------------------------------------
# Exercise 9: Password Strength Checker
# Create a program that takes a password as input and checks its
# strength based on the following rules:

# If the password is less than 8 characters, print "Weak password."
# If the password is 8 to 12 characters long, print "Moderate password."
# If the password is more than 12 characters, print "Strong password

# You can use len() function to get the length of a given string.

password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password")
elif 8 <= len(password) <= 12:
    print("Moderate password.")
elif len(password) > 12:
    print("Strong password")

# ---------------------------------------------------------------------
# CHALLENGE (OPTIONAL): Course Enrollment Eligibility
# To solve this exercise, you will need to use the following concepts
# and methods:
# - String method .upper()
# - String slicing
# - if-elif-else conditional statements
#
# You're designing a course enrollment system. Write a program that
# takes a course code and a student's grade as input and determines
# whether the student is eligible to enroll in the course.

# 1. Ask the user to enter a course code (e.g., "CS101", "MATH202", ).
#    All courses ends with "101", "202" or "303". Slice the string
#    to get the last three character of the string to get the course
#    ending:
#
#    Hint:
#    test = "ABCDEF"  # Given this string
#    print(test[-2:])  # It will print "EF"

# 2. Ask the user to enter their grade (e.g., "A", "B", "C", "D", "F").
#    Use .upper() method to convert the course code and grade to uppercase,
#    allowing for case-insensitive input.
#
# Implement the following enrollment rules:
# - For courses with course codes ending in "101", students with
#   grades "A" or "B" are eligible.
# - For courses with course codes ending in "202", students with
#   grades "B" or "C" are eligible.
# - For courses with course codes ending in "303", students with
#   grades "C" or "D" are eligible.

# Print either "You are eligible to enroll." or "You are not eligible to enroll."
course_code = input("Enter the course code, CS101, CS202, or CS303: ")
student_grade = input("Enter your grade: ")

# Convert input to uppercase for case-insensitive comparison
course_code = course_code.upper()
student_grade = student_grade.upper()

# Extract the last three characters of the course code (use string slicing)
course_suffix = course_code[2:]
print('Course suffix is: ' + course_suffix)

# Check course code and grade to determine eligibility
eligible = False
if course_suffix == "101":
    if student_grade.upper() in ('A', 'B'):
        eligible = True
elif course_suffix == "202":
    if student_grade.upper() in ('A', 'B', 'C'):
        eligible = True
elif course_suffix == "303":
    if student_grade.upper() == 'A':
        eligible = True
if eligible:
    print('You may enroll.')
else:
    print('You are not eligible to enroll.')# <Your code here>


