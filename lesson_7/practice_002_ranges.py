# Figure out the values required for range() to generate the expected result:

# 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# 20, 21, 22 ... 30 (all the numbers between 20 and 30, inclusive)
for i in range(20, 31):
    print(i)

# Even numbers: 2, 4, 6, 8, 10
for i in range(0, 10, 2):
    print(i)

# Years ending in zero between 1900 and 2000 (inclusive)
for i in range(1900, 2010, 10):
    print(i)

# Bonus!
# 20, 19, 18, 17, 16
for i in range(20, 15, -1):
    print(i)