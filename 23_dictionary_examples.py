#Dictionary is a collection of "Key-Value pairs".
#Key = unique (duplicates are not allowed).
#Value = can be anything (string, number, list, dictionary).
#Dictionary is written in curly braces {}.

#example:--
student = {
    "name": "Sammed",
    "age": 21,
    "course": "BCA"
}
print(student)
# Output: {'name': 'Sammed', 'age': 21, 'course': 'BCA'}

..........................................................

    #Types of dictionary creation:--

    # Normal way
d1 = {"a": 1, "b": 2, "c": 3}
print(d1)  #output:{'a': 1, 'b': 2, 'c': 3}


# Using dict() function
d2 = dict(x=10, y=20, z=30)
print(d2)   # {'x': 10, 'y': 20, 'z': 30}  #output:{'x': 10, 'y': 20, 'z': 30}


# Nested dictionary
d3 = {"person": {"name": "Sammed", "age": 21}}
print(d3) #output:{'person': {'name': 'Sammed', 'age': 21}}

