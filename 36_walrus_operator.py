##Walrus Operator
#In Python, the Walrus Operator := is called Assignment Expression.

#Storing the value and committing it in a single line.

#Without Walrus Operator:  x = 10        # पहले x में मान डाला
if x > 5:     # फिर उस मान का उपयोग किया
    print(x)
 output:10

.....................................................................

#With Walrus Operator:

if (x := 10) > 5:   # यहाँ x में 10 भी डाल दिया और तुरंत उसका उपयोग भी कर लिया
    print(x)
output: 10


#Advantage → Code becomes shorter and cleaner.


#Remember this step:
#= meaning only to keep value
#:= keeping value + using it at the same time



#Just put the item in the "box".
(Normal =)

x = 5     put 5 named x 
print(x)    then used it   

.....................................................

Walrus := Keep the item pressed and use it immediately.

    print(x := 5)   #5 Save it and print it immediately
    output:5






