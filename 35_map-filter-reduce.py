#map_filter_reduce 

#1) map() → हर element को बदलना
(Produces a new result by performing an operation on each element of a list/array.)

numbers = [1, 2, 3, 4, 5]

# हर नंबर का square निकालना
squares = list(map(lambda x: x**2, numbers))
print(squares)                                # [1, 4, 9, 16, 25]


.......................................................................................

2) filter() → Select by applying condition

"Retains only those values ​​from the list/array that satisfy the condition"
Meaning → The entire list will be checked, but the result will return only those values ​​that pass the rule/condition.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# condition: सिर्फ even numbers चाहिए (जो 2 से divide हों)
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

[2, 4, 6, 8, 10]

........................................................................................



  3) reduce() → Combines all the values ​​to create a single value.

 Combines the entire list step by step and returns a single final value.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# सभी नंबरों का sum निकालना
total = reduce(lambda a, b: a + b, numbers)
print(total)   # 15


