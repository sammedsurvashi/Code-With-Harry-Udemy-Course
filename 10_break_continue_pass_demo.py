##Break, Continue, Pass in Python

#break → Stops the loop completely.
#continue → Skips the rest of the code in the current iteration and goes to the next.
#pass → Does nothing; used as a placeholder.


for i in range(5):
    if i == 2:
        continue  # skip when i is 2
    if i == 4:
        break            #stop when i is 4
    print(i)

# pass example
for i in range(3):
    pass            # placeholder for future code

output:
0
1
3

........................................................
#pass examples
    for i in range(3):
    pass                  #Here there is no code, just a placeholder

# Meaning of pass:
# pass means — "do nothing".
# It is used when you want to leave a block of code empty so you can write something later.
# In Python, an empty block is not allowed, so we use pass.


.................................................................................

break → Immediately stops the loop and exits it.
continue → Skips the current iteration and moves to the next iteration of the loop.

    for i in range(1, 6):
    if i == 3:
        continue  # Skip number 3
    if i == 5:
        break     # Stop the loop at 5
    print(i)

output :-
1  
2  
4





