import re

# string and string functions
str1 = "Michael Jordan is the best"
print(f"{str1}\n")

# multiline string
str2 = """This
is
a
multiline
string"""
print(f"{str2}\n")

# slicing
# strides - get every Nth chars starting from 0
print(f"string stride; print every 2nd char starting from 0:\n{str1[::2]}\n")
print(f"reverse string with stride [::-1]:\n{str1[::-1]}\n")

# substring - get [n, m) chars inclusive
print(f"substring from [n, m) => [8, 14):\n{str1[8:14]}\n")
print(f"substring from beginning to N => [0, 6):\n{str1[:7]}\n")
print(f"substring from N to end => [8, end):\n{str1[8:]}\n")
print(f"reverse indexing [-18:-12]:\n{str1[-18:-12]}\n")

