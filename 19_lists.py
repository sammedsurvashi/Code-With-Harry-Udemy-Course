#A list is a collection of items in Python.
#Lists are ordered, mutable (changeable), and allow duplicate values.
#Created using square brackets [ ].


#Creating a List

my_list = [10,20,30,"Hello",3.14]
print(my_list)                           #[10,20,30,"Hello",3.14]
print(type(my_list))                       #<class 'list'>

====================================================================================

# 1. append(x)
# English: Adds an element at the end of the list
# Hindi: लिस्ट के अंत में नया element जोड़ता है
lst = [1, 2, 3]
lst.append(4)
print(lst)   # [1, 2, 3, 4]

# 2. insert(i, x)
# English: Inserts an element at a specific index
# Hindi: किसी index पर नया element जोड़ता है
lst.insert(1, 99)
print(lst)   # [1, 99, 2, 3, 4]

# 3. remove(x)
# English: Removes the first occurrence of the element
# Hindi: दिए गए element को हटाता है
lst.remove(99)
print(lst)   # [1, 2, 3, 4]

# 4. pop(i)
# English: Removes element by index (default last)
# Hindi: Index का element हटाता है (default: आखिरी)
lst.pop()
print(lst)   # [1, 2, 3]

# 5. clear()
# English: Removes all elements from the list
# Hindi: लिस्ट के सभी elements हटाता है
lst.clear()
print(lst)   # []

# 6. sort()
# English: Sorts the list in ascending order
# Hindi: लिस्ट को छोटे से बड़े क्रम में सजाता है
lst = [4, 1, 3, 2]
lst.sort()
print(lst)   # [1, 2, 3, 4]

# 7. reverse()
# English: Reverses the list order
# Hindi: लिस्ट को उल्टा करता है
lst.reverse()
print(lst)   # [4, 3, 2, 1]

# 8. index(x)   #[Important: Index हमेशा 0 से शुरू होता है.]
# English: Returns index of the element
# Hindi: Element का index बताता है
print(lst.index(3))   # 1

# 9. count(x)
# English: Counts how many times an element occurs
# Hindi: Element कितनी बार है ये गिनता है
print(lst.count(2))   # 1

# 10. copy()
# English: Creates a shallow copy of the list
# Hindi: लिस्ट की कॉपी बनाता है
new_lst = lst.copy()
print(new_lst)   # [4, 3, 2, 1]

