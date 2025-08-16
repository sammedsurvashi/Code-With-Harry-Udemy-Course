#Two types of modules in python 
# --Built-in modules
# --External Modules

 #What is a Module?
#A module in Python is a file that contains functions, variables, or classes, which can be reused in other programs.

 Types of Modules

# 1. Built-in Modules
These come pre-installed with Python.

#Example:
```python
import math
print(math.sqrt(25))   # 5.0

....................................

2. User-Defined Modules ✍️

These are created by the user.
def greet(name):
    return f"Hello, {name}!"

////////////////////////////////////////////

import my_module
print(my_module.greet("Sammed"))  # Hello, Sammed!

.............................................................

#3.External (Third-Party) Modules 📦

These are not included in Python by default.
They must be installed using pip (Python package manager).

        pip install numpy

import numpy as np
arr = np.array([1, 2, 3])
print(arr)   # [1 2 3]



#Built-in Module → Already in Python (math, os, random)

#User-Defined Module → Created by the user (my_module.py)

#External Module → Installed using pip (numpy, pandas, matplotlib)


