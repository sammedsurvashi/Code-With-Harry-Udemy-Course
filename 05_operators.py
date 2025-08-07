# 1. Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators")

print("Addition:", a + b)           # 13
print("Subtraction:", a - b)        # 7
print("Multiplication:", a * b)     # 30
print("Division:", a / b)           # 3.333...
print("Modulus:", a % b)            # 1
print("Exponent:", a ** b)          # 1000
print("Floor Division:", a // b)    # 3

=============================================================================================
# 2. Comparison Operators
a = 5
b = 7

print(" Comparison Operators")
print("Equal:", a == b)             # False
print("Not Equal:", a != b)         # True
print("Greater:", a > b)            # False
print("Less:", a < b)               # True
print("Greater or Equal:", a >= b) # False
print("Less or Equal:", a <= b)     # True
=================================================================================================
# 3. Logical Operators
x = 10

print(" Logical Operators")
print("AND:", x > 5 and x < 15)     # True
print("OR:", x < 5 or x < 15)       # True
print("NOT:", not(x < 15))          # False
=================================================================================================
# 4. Assignment Operators
a = 5

print(" Assignment Operators")
print("Original a:", a)             # 5
a += 3
print("a += 3:", a)                 # 8
a *= 2
print("a *= 2:", a)                 # 16
a -= 4
print("a -= 4:", a)                 # 12
a /= 2
print("a /= 2:", a)                 # 6.0
====================================================================================================
# 5. Membership Operators
name = "Sammed"

print(" Membership Operators")
print("'a' in name:", 'a' in name)         # True
print("'z' not in name:", 'z' not in name) # True
=====================================================================================================# 6. Identity Operators
# 6. Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("🔸 Identity Operators")
print("x is y:", x is y)     # True (same object)
print("x is z:", x is z)     # False (different object)
print("x == z:", x == z)     # True (same content)





