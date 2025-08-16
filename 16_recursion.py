#“Recursion is when a function calls itself until a base case stops it.
(#Recursion वह प्रक्रिया है जिसमें कोई function खुद को बार-बार call करता है, जब तक base case न आ जाए)

#Example – Number Countdown.

  def coutdown(n):
#base case (stopping condition)

if n == 0;
print("Done!")
return

#work
print(n)

#recursion case (function calls itself)
countdown(n - 1)

countdown(5)

#output : 
5
4
3
2
1
Done!
