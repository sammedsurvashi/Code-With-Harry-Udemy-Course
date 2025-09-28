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

..............................................................................................

#2) **kwargs (keyword arguments)

#This is used when values ​​are to be given in the form of key-value pairs.

#**kwargs means to get values ​​by storing them in a dictionary.

def show_details(**kwargs):
    print(kwargs)  # dictionary मिळते
    for key, value in kwargs.items():
        print(key, "=", value)

show_details(name="Sammed", age=21, city="Pune")

#The values ​​in kwargs are in dictionary format:
{'name': 'Sammed', 'age': 21, 'city': 'Pune'}



#Easy to remember:

*args 👉 multiple values ​​(makes a tuple)
**kwargs 👉 multiple key = value (makes a dictionary)

...............................................................................

#Example: *args + **kwargs together

def demo_function(*args, **kwargs):
    print("Args (tuple):", args)       # फक्त values
    print("Kwargs (dict):", kwargs)    # key=value जोडी

#वापर
demo_function(10, 20, 30, name="Sammed", age=21, city="Pune")

output:Args (tuple): (10, 20, 30)
Kwargs (dict): {'name': 'Sammed', 'age': 21, 'city': 'Pune'}













