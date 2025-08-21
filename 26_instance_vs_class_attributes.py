class Car:
    # Class Attribute (सर्व objects साठी समान)
    wheels = 4

    def __init__(self, name, color):
        # Instance Attributes (प्रत्येक object साठी वेगळे)
        self.name = name
        self.color = color

# Objects तयार करतो
c1 = Car("BMW", "Black")
c2 = Car("Audi", "White")

# Access values
print(c1.name, c1.color, c1.wheels)
print(c2.name, c2.color, c2.wheels)

........................................

 #Explanation 

class Car:
→ Car नावाचा Class तयार केला (blueprint).

wheels = 4
→ हे एक Class Attribute आहे → सर्व objects ला एकच value (4 wheels).

def __init__(self, name, color):
→ Constructor function, object तयार होताना चालतं.

self.name = name & self.color = color
→ हे Instance Attributes आहेत → प्रत्येक object ला वेगळं नाव आणि रंग मिळतो.

c1 = Car("BMW", "Black")
→ पहिला object तयार केला → c1.name = "BMW", c1.color = "Black".

c2 = Car("Audi", "White")
→ दुसरा object तयार केला → c2.name = "Audi", c2.color = "White".

print(c1.name, c1.color, c1.wheels)
→ BMW Black 4 print होतं.

print(c2.name, c2.color, c2.wheels)
→ Audi White 4 print होतं.

..................................................
..................................................
#Instance Attributes = वेगवेगळ्या object ला वेगळं data.
#class Attribute = सर्व objects साठी समान data.



