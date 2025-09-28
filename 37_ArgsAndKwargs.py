#1) *args (arguments)

#This is useful when you don't know in advance how many values ​​to pass to a function.

#*args means to get multiple values ​​by putting them in a tuple.

#Example:
def add_numbers(*args):
    print(args)  # tuple मिळते
    return sum(args)

print(add_numbers(1, 2, 3))       # 6
print(add_numbers(10, 20, 30, 40)) # 100

#The values ​​in args are in the form of a tuple: (1,2,3)
