#Lambda function in Python = a small, anonymous (nameless) function written in one line using lambda


# Normal function to add two numbers.                         # Same work using lambda
                                                               add = lambda a, b: a + b
                                                                print(add(5, 3))   # Output: 8
def add(a, b):
    return a + b

print(add(5, 3))   # Output: 8


#Normal function → uses def, can have multiple lines, has a name.
#Lambda function → uses lambda, single line, mostly used for short/temporary work.
