'''Write a Python class,

MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.

Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type

If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class'''


class MedPlus:
    def __init__(self, name:str, num:int, price: float):
        if not isinstance(name, str):
            raise Typeerror("Name must be a string")
        if not isinstance (num, int):
            raise Typeerror("Number must be an integer")
        if not isinstance(price, float):
            raise Typeerror("Price must be in float type")       
        self.name = str(name)
        self.num = int(num)
        self.price = float(price)
    
a=MedPlus("tisha",12,12.4)
a.name
a.num
a.price
print(a.name,+a.num,+a.price)