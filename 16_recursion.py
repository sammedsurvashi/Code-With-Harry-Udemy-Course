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

जब countdown(5) चलता है → यह 5 प्रिंट करता है, फिर countdown(4) को call करता है।
countdown(4) 4 प्रिंट करता है, फिर countdown(3) को call करता है।
यह process ऐसे ही चलता रहता है जब तक n 0 नहीं हो जाता।
जब n == 0 होता है, तब base case मिल जाता है → यह "Done!" प्रिंट करता है और recursion रुक जाता है।

