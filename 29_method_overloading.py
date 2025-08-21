#2. Method Overloading #एका class मध्ये एकाच नावाचे वेगवेगळ्या parameters असलेले methods असतील तर त्याला method overloading म्हणतात.
                       #If a class has methods with the same name and different parameters, it is called method overloading.
#एकाच method ला वेगवेगळ्या arguments नी वापरणं
#Python मध्ये direct नाही, पण default arguments वापरतो

....................................................................
class Calculator:
    def add(self, a, b=0, c=0):  # एकच method (default values दिल्या)
        return a + b + c

calc = Calculator()

print(calc.add(5, 10))      # Output: 15  (2 numbers add केले)
print(calc.add(5, 10, 15))  # Output: 30  (3 numbers add केले)

#Explanation:--

#add() एकच method आहे
#arguments वेगवेगळे दिले तरी काम वेगळं होतं
#म्हणजे हेच Overloading सारखं
