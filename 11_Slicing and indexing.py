#Indexing: To access each character in a string, we use an index (starts from 0, and -1 means the last character).

#Slicing: To take a part of a string, we use [start:end] (the end index character is not included).

text = "Python"

# Indexing
print(text[0])   # Output: P (पहला अक्षर)
print(text[-1])  # Output: n (आखिरी अक्षर)

# Slicing
print(text[0:4])  # Output: Pyth (0 से 3 तक के अक्षर)
print(text[2:])   # Output: thon (इंडेक्स 2 से आखिरी तक)
print(text[:3])   # Output: Pyt (शुरुआत से 2 तक)


#Indexes are of two types:

Positive Index – Starts from 0 from the left side (beginning of the string).
Negative Index – Starts from -1 from the right side (end of the string). 

...................................................................................

  # Example string
name = "PYTHON"

# Positive Indexing
print(name[0])   # P (first letter)
print(name[1])   # Y
print(name[5])   # N (last letter)

# Negative Indexing
print(name[-1])  # N (last letter)
print(name[-2])  # O
print(name[-6])  # P (first letter)

output:

P
Y
N
N
O
P

#Positive index → counts from left (0, 1, 2, …)
#Negative index → counts from right (-1, -2, -3, …)

