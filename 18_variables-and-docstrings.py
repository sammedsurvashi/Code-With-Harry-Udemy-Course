#Variable Scope and Docstrings in Python

#Variable Scope:-
#Scope defines where a variable can be accessed in a program.

#Types of Scope in Python

#1.Local Scope --    Defined inside a function, accessible only there.
                                                                                 def my_func():
                                                                                  x = 10   # Local
                                                                                  print(x)
   def func():                                                                    my_func()   # 10
  x = 10   # Local variable
    print("Inside:", x)

func()
# print(x)  Error (x not accessible outside)
......................................................................


#2.Enclosed Scope   . Defined outside functions, accessible everywhere.
  def outer():
    x = 20   # Enclosed
    def inner():
        print(x)   # inner uses outer’s variable
    inner()

outer()   # 20
...........................................................................

#3.Global Scope __   Variable defined outside all functions, usable anywhere in the file.
x = 30   # Global

def my_func():
    print(x)   # can access global

my_func()   # 30

....................................................

  
#4.Built-in Scope -- Python’s predefined names/functions available everywhere.

  print(len([1, 2, 3]))   # 3
  print(sum([5, 10, 15])) # 30

  
 LEGB Rule → Variable lookup order:
                       L → Local → Enclosed → Global → Built-in
