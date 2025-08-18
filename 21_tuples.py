#Tuple is similar to a list but immutable (its values cannot be changed).


a = (3,2,22,13)

print(a)
print(a[2])  #output:22

#but
a [3] =32     #a[3] is 13
#error: typeerror tuple object does not support item assignment(can't change)
