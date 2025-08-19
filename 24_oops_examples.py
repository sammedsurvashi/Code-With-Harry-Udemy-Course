#Object-Oriented Programming (OOP) in Python:--
{#OOP (Object-Oriented Programming) is a programming style where we organize code using Classes (design) and Objects (real things).

#OOP म्हणजे अशी programming style जिथे आपला code आपण Class (नकाशा/डिझाईन) आणि Object (प्रत्यक्ष वस्तू) वापरून व्यवस्थित ठेवतो.}

  1.Class:-Class is just a design or blueprint.

# Example of Class
class Car:   # <-- हे class आहे
    def __init__(self, name, color):   # Constructor (class सुरू होताना चालतो)
        self.name = name   # Attribute #(गुणधर्म)
        self.color = color # Attribute 
.......................................................................................

  2.Object:--     
#Object is the real thing created from the class.
#Object म्हणजे class वरून तयार झालेली प्रत्यक्ष वस्तू.

# Example of Object
c1 = Car("BMW", "Black")   # <-- हे Object आहे
c2 = Car("Audi", "White")  # <-- हे दुसरं Object आहे.
.........................................................................................

3.Encapsulation:-- (Putting Data + Methods Together)
# Encapsulation means keeping data and methods together in one unit.
 #Encapsulation म्हणजे Data आणि Methods एकत्र ठेवणे आणि काही माहिती लपवणे.

class Student:   # Class तयार केला
    def __init__(self, name, marks):
        self.name = name    # Data (नाव)
        self.marks = marks  # Data (गुण)
    
    def show(self):         # Method (function)
        return f"{self.name} has {self.marks} marks"
    

s1 = Student("Sammed", 95)   # Object तयार केला
print(s1.show())  

                                  #Student class मध्ये → Data (name, marks) आणि Method (show) एकत्र आहे.
                                  #s1 Object ने हे वापरले.
                                  #ह्यालाच म्हणतात Encapsulation (Data + Methods एकत्र ठेवणे).




4.Inheritance:--
 #Inheritance means using the properties of one class into another.
 #Inheritance म्हणजे एका class चे गुणधर्म दुसऱ्या class मध्ये वापरणे.

class Car:   # Parent Class
    def __init__(self, name, color):
        self.name = name
        self.color = color


class ElectricCar(Car):   # Child Class (Car पासून गुण घेतो)
    def __init__(self, name, color, battery):
        super().__init__(name, color)   # Parent (Car) ची properties घेतल्या
        self.battery = battery          # Extra property जोडली
    

e1 = ElectricCar("Tesla", "White", "85kWh")
print(e1.name, e1.color, e1.battery)  
#Car → Parent class.

                                         #ElectricCar → Car चे सर्व गुणधर्म घेतले + नवीन (battery) जोडले.
                                         #ह्यालाच म्हणतात Inheritance (गुण वारसा मिळवणे).






5.Polymorphism:--
#Polymorphism means one thing working in different ways.
#Polymorphism म्हणजे एकच गोष्ट वेगवेगळ्या प्रकारे काम करणं.

class BMW(Car):   # BMW Class
    def sound(self):       # Method
        return "BMW goes Vroom!"


class Tesla(Car):   # Tesla Class
    def sound(self):       # Method
        return "Tesla goes Whirr!"
    

b = BMW("BMW", "Black")     # BMW Object
t = Tesla("Tesla", "White") # Tesla Object

print(b.sound())   # BMW goes Vroom!
print(t.sound())   # Tesla goes Whirr!

                                          दोन्ही classes मध्ये method sound() नावाचा आहे.
                                          पण BMW → Vroom! आवाज काढतो, Tesla → Whirr! आवाज काढतो.
                                          ह्यालाच म्हणतात Polymorphism (एकच गोष्ट → वेगवेगळ्या प्रकारे काम करणे).

================================================================================================================





#Class → Blueprint / Design (नकाशा)
#Object → Class वरून तयार झालेली वस्तू (Instance)
#Encapsulation → Data + Methods एकत्र (Security)
#Inheritance → एका class चे गुणधर्म दुसऱ्यात (Code reuse)
#Polymorphism → एकच गोष्ट वेगवेगळ्या प्रकारे काम करणं


