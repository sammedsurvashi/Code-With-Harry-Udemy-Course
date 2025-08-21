 #Inheritance and Polymorphism

1. Inheritance : (वारसा मिळवणं)   #एका class चे गुणधर्म दुसऱ्या class ला मिळणे.
                                #म्हणजे Child class → Parent class कडून properties घेते.
..............................................................................................


# Parent Class
class Car:   # Car नावाचा parent class
    def __init__(self, name, color):   # Constructor → कारचं नाव आणि रंग ठेवतो
        self.name = name
        self.color = color
    
    def show(self):   # Method → कारचं info परत करतो
        return f"Car: {self.name}, Color: {self.color}"

# Child Class (inherits Car)
class ElectricCar(Car):   # ElectricCar हा Car class वरून तयार झालेला Child आहे
    def __init__(self, name, color, battery):   
        super().__init__(name, color)   # Parent (Car) चं constructor वापरतो
        self.battery = battery         # नवं attribute (battery) add केलं
    
    def show_battery(self):   # Child class ची खास method
        return f"{self.name} has a {self.battery} kWh battery."

# Object तयार करणे
e1 = ElectricCar("Tesla", "White", 85)   # Tesla नावाचं ElectricCar object

print(e1.show())          # Parent class मधलं method कॉल केलं
print(e1.show_battery())  # Child class मधलं method कॉल केलं

#output 
Car: Tesla, Color: White
Tesla has a 85 kWh battery.

