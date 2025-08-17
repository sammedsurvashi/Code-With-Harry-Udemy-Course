#List comprehension is a short and clean way to create new lists in Python using a single line of code.
#Hindi:- 
#List comprehension Python में नई लिस्ट बनाने का शॉर्ट और आसान तरीका है, सिर्फ़ एक लाइन में।

#syntax:-- [expression for item in iterable if condition]

#expression → what to do (e.g., find square)
#item → element (like x)
#iterable → list, range, string, etc.
#condition (optional) → used to apply a filter

squares = [x*x for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

#explain:-- Here range(5) means → [0, 1, 2, 3, 4]

When x = 0 → 0*0 = 0
When x = 1 → 1*1 = 1
When x = 2 → 2*2 = 4
When x = 3 → 3*3 = 9
When x = 4 → 4*4 = 16

 #Output: [0, 1, 4, 9, 16]

=====================================================================

evens = [x for x in range(10) if x % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8]



#Here range(10) means → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Condition if x % 2 == 0 means x should be divisible by 2 (even number).
#So the list comprehension will take only even numbers → [0, 2, 4, 6, 8]

Simple understanding:--
First example → generates squares.
Second example → filters even numbers.

