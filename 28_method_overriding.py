#Method Overriding

#Parent class मध्ये असलेली method → Child class मध्ये पुन्हा लिहिणे (rewrite)
#Method name same, काम वेगळं
......................................................................

class Car:   # Parent class
    def sound(self):      # Parent method
        return "Car makes normal sound"

class Tesla(Car):         # Child class
    def sound(self):      # Overriding केली (Parent method बदलली)
        return "Tesla makes electric sound"

c = Car()
t = Tesla()

print(c.sound())   # Output: Car makes normal sound  (Parent ची method चालली)
print(t.sound())   # Output: Tesla makes electric sound (Child ने override केलं)

...............................
...............................
#Explanation:--

#Car → sound() method आहे
#Tesla → Car पासून Inherit झालं
#पण Tesla मध्ये sound() वेगळं लिहिलं → यालाच Overriding
===================================================================================================


