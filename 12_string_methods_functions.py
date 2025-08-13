name = "Sammed"             #stings are immutable

#name[0] = "R"              #you cannot do this 

a = len(name)
print(a)

output: 6

.........................................................

1. upper() #convers lowercase letters to  uppercase

name = "sammed"
print(name.upper())
output : SAMMED
..................................

2. lower() #converts uppercase letters to lowercase

name = "SAMMED"
print(name.lower())
output: sammed
.................................

3.capitalize () #makes only the first letter of the word uppercase

text = "sammed survashi"
print(text.capitalize())
output : Sammed survashi
................................

4.title() #makes the first letter of each word uppercase 

text = "my name is sammed"
print(text.title())
output: My Name Is Sammed
................................

5.strip()       #Removes spaces from the beginning & end 

name = "  sammed  "
print(name.strip())
output: sammed
.
.  * lstrip()   #Removes spaces from the beginning only

    name = "   Sammed   "
    print("lstrip():", repr(name.lstrip()))
    output:'sammed  '
.
.
  * rstrip       #Removes spaces from the end only
    name = "   Sammed   "
    print("rstrip():", repr(name.rstrip()))
    output: '  sammed'
........................................................

6. replace() #Replace one word with another word.
fruit = "I eat mango"
print(fruit.replace("mango","apple"))
output: I eat apple
....................................................

7.split() #joins list elements into a string (स्ट्रिंगला तुकडे करून लिस्टमध्ये ठेवण्यासाठी वापरली जाते.)
data = "red,green,blue"
print(data.split(",")) 
output:['red','green','blue']
.............................................

8.join()   #Joins list elements into a string
colors =['red','green','blue']
print"-".join(colors))
output: red-green-blue
.............................................

9.find() #Returns the starting position of a word 
    sentence = "I love python"
print(sentence.find("python"))
output: 7














