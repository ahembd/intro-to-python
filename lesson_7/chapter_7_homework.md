# Homework: Loops

🔥 **Read carefully until the end before you start solving the exercises.** 🔥

## Practice the Basics 💪🏻

### Create a basic `for` loop

Complete the following code in such a way that this loop prints the characters 
of `name` one at a time.


name = "Joseph"

for letter in name:
    print(letter)


### Create a basic `for` loop with a counter

#Complete the following code in such a way that the loop increments the
#counter and prints the number of characters in `name` at the end.


name = 'Tom'
counter = 0

for i in name:
    print(i)
    counter = counter++

# This should print '3'
print(counter)


### Create a basic `while` loop

#Complete the following code in such a way that the loop exits after **five**
#iterations, _without_ using `break`

#🔥 **Hint**: Think of it as: _while counter is under 5, increment the counter and print its value_ 🔥

i = 1
counter = i
while i < 5:
    print(name[i])
    i++
    

while counter > 0:
    print(counter)
    counter--
```

### Exit a loop using `break` 🛑

##Take the previous example, and modify it so you exit the loop after **five** iterations, 
##but this time do it _using_ `break`

counter = len(name)

while counter > 0
    counter--

    if count < len(name):
        break
        
    print(counter)


### Range

#Remember that `range(start, end, step)` behaves somewhat like list slicing, so `start` is inclusive,
`end` is exclusive, and `step` is optional.

#Figure out the values required for `range()` to generate the expected output.
# 0, 1, 2, 3, 4, 5 (use only one argument)
range(6)

# 0, 1, 2, 3, 4, 5 (use two arguments: start and end)
range(0,6)

# Odd numbers between 0 and 10: 1, 3, 5, 7, 9
range(???)
```

### Using `range()` in a loop

Remember that `range()` returns an _iterable_, so you will usually find it used in a `for` loop.

Complete the following code so it prints the _even_ numbers between 0 and 10;

```python
for num in range(0,10):
    if num%2 == 0:
        print(num)
```

## Exercises 🏋🏻

### Digits Only!

**Part one**: Given a string of letters and digits, complete the program to print only the digits. 
For example, for the string `3catsand5tacos`, output should be: 3 5

Strategy:
- Create variable to hold the string: `my_string = '3catsand5tacos'`
- Create a string to represent the numbers: `numbers = '1234567890'`
- Create a loop to iterate through characters of `my_string`. 
If the character is a digit (`if character in numbers`) print it.

```python
my_string = 's0m3 str1ng w1th numb3r5'
numbers = '1234567890'

for character in my_string:
    if character in numbers:
        print(character)
```

**Part two**: Modify the code to print **the first digit only**

### Vowel Counter

Imagine you're working on a text analysis tool that needs to count the number of vowels in a given string. 
As a simple practice, you have been provided with a famous quote. Your task is to count and display the total 
number of vowels in this quote.

```python
quote = "Life is like riding a bicycle. To keep your balance, you MUST keep moving."
vowel_count = 0

for letter in quote:
    # 'A' and 'a' are different in python, so we include both upper and lowercase
    # vowels in our comparison string to account for this difference.
    if letter in 'aeiouAEIOU':
        vowel_count = vowel_count + 1

print(f"The number of vowels in the quote is: {vowel_count}")
```

### Sum of all Digits 🔢

You have a mixed string that contains both letters and numbers, like an alphanumeric password or 
a serial key. Your task is to find all the numbers in this string and sum them up.

**Hint**: You can put the numbers you find into a list (cast as `int`) and use `sum()` on the list at the end.

```python
mixed_string = "abc123xyz456"
digits = "0123456789"
found_digits = []

for char in mixed_string:
    if char in digits:
        found_digits.append(int(char))

print(f"The total sum of numbers in the string is: {sum(found_digits)}")
```

### Password Strength Checker

You are helping to develop a user registration page for a website. As part of the registration process, 
you need to ensure that submitted passwords are strong. A strong password should have **at least 8 characters**.

Create a Python program to check the strength of a list of passwords and count how many are strong.

```python
passwords = ['Passw0rd', 'hello', 'strongPass1', 'weak']
strong_password_count = 0

for i in password:
    if len(password) >= 8:
        strong_password_count += 1

print(f"Number of strong passwords: {strong_password_count}")

```

###  The Red Crayon 🖍️

#Imagine you have a box of crayons, and you're #looking for a "Red" crayon. 
#You pull out one crayon at a time from the box. 

#Use a `while` loop to simulate this scenario.  #As soon as you find the "Red" crayon, stop #the loop.


colors = ["Blue", "Yellow", "Green", "Red", "Purple", "Orange"]
index = 0

# This should basically say: while the current color being evaluated is 
# different than "Red", increment to the next color and try again.
while colors[index] != "Red":
    print(f"Found {colors[index]} crayon. Still looking for Red.")
    index += 1

print("Found the Red crayon!")
