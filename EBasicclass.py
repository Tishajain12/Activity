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