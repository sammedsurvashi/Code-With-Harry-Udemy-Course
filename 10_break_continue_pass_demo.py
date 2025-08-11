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

