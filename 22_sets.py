#Sets in Python

#Set = Unordered collection of unique elements (duplicates not allowed).

#Example:
my_set = {1, 2, 3, 4, 4}
print(my_set)   # {1, 2, 3, 4} (duplicates removed)

# Normal set
s1 = {1, 2, 3}        
print(s1)   # {1, 2, 3}

# Using set() function
s2 = set([4, 5, 6])   
print(s2)   # {4, 5, 6}

# {} creates dictionary, not set
s3 = {}
print(type(s3))   # <class 'dict'>

# Empty set
s4 = set()
print(type(s4))   # <class 'set'>
.....................................

2.Union ( a | b )

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # {1, 2, 3, 4, 5}
#Removes duplicates by combining both sets.
....................................................

3.Intersection ( a & b )  
#Only keep elements that are common to both sets.

a = {1, 2, 3}
b = {3, 4, 5}

print(a.intersection(b))   # Output: {3}
print(a & b)               # Output: {3} 
........................................................

4. Difference(a - b)
#a - b means that which is in a but not in b.

  a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a.difference(b))   # Output: {1, 2}
print(a - b)             # Output: {1, 2}

print(b.difference(a))   # Output: {5}
print(b - a)             # Output: {5}
...............................................

5.Symmetric Difference #(Only those elements that are not common remain)
                        # Elements that are between both sets but are not common.

a = {1, 2, 3}
b = {3, 4, 5}

print(a.symmetric_difference(b))   # Output: {1, 2, 4, 5}




