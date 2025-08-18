#Tuple is similar to a list but immutable (its values cannot be changed).


a = (3,2,22,13)

print(a)
print(a[2])  #output:22

#but
a [3] =32     #a[3] is 13
#error: typeerror tuple object does not support item assignment(can't change)

..................................................

1.#creating a tuple

my_tuple = (10,20,30)  #Tuples are created using () (parentheses).
single_element = (5,) #tuple with one element comma required.

.......................................................

  2.#Accessing Elements (Indexing – घटक काढणे
  t = (1, 2, 3, 4)
print(t[0])   #1 (first element)
print(t[-1])  #4 (last element)
#or
t = (10, 20, 30, 40, 50)
print(t[0])    # 10
print(t[-1])   # 50
print(t[1:4])  # (20, 30, 40)
......................................................

3.#*Operations (+ , )
+ = Join / Add tuples
* = Repeat tuple elements

fruits1 = ("apple", "mango")
fruits2 = ("banana", "orange")

print(fruits1 + fruits2)   # ('apple', 'mango', 'banana', 'orange')
print(fruits1 * 2)         # ('apple', 'mango', 'apple', 'mango')
...............................................................

4.#Functions (len, max, min, sum)
#Common functions work on tuples.

t = (5, 10, 15)

print(len(t))   # 3   (length / number of elements)
print(max(t))   # 15  (maximum / largest value)
print(min(t))   # 5   (minimum / smallest value)
print(sum(t))   # 30  (sum / total of all values)
............................................................
5.#Methods (count, index)
#There are only two methods in a tuple

t = (1, 2, 2, 3)
print(t.count(2))   # 2 occurs 2 times / 2 दो बार आया
print(t.index(3))   # index = 3 / position 3 पर है
.................................................................

6.Packing & Unpacking.
Packing = put values in tuple.
Unpacking = take values out.

t = 10, 20, 30    # Packing
a, b, c = t       # Unpacking
print(a, b, c)    # 10 20 30





