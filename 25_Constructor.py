#What is a constructor?
#A constructor is a special method.
#In Python, it is called __init__().
#This method runs automatically when an object is created.
#That is, the constructor does its initial setup when an object is created.

#Syntax:-
class ClassName:
    def __init__(self, parameters):
        self.variable = parameters



class Car:
    # Constructor
    def __init__(self, name, color):
        self.name = name      # attribute (object चं नाव)
        self.color = color    # attribute (object चा रंग)

# Objects तयार झाले म्हणजे constructor आपोआप चालेल
c1 = Car("BMW", "Black")
c2 = Car("Audi", "White")

print(c1.name, c1.color)   # BMW Black
print(c2.name, c2.color)   # Audi White


