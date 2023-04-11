
'''Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)'''
a=int(input())
b=int(input())
def add(a,b):
    c=a+b
    return c
print("Addition:",add(a,b))
def subtract(a,b):
    c=a-b
    return c
print("Subtraction:",subtract(a,b))
def multiply(a,b):
    c=a*b
    return c
print("Multiplication:",multiply(a,b))
def divide(a,b):
    c=a/b
    return c
print("Division:",divide(a,b))
def power(a,b):
    c=a**b
    return c
print("Power:",power(a,b))
def remainder(a,b):
    c=a%b
    return c
print("Remainder:",remainder(a,b))
def float_division(a,b):
    c=a+b
    return c
print("Float division:",float_division(a,b))

'''Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3)'''
a=float(input("Enter distance in Kilometers: "))
def centimeters(a):
    conversion=a*100000
    return conversion
print(centimeters(a),"cm")
def km_meter(a):
    conversion=a*1000
    return conversion
print(km_meter(a),"meters")
b=float(input("Enter the weight of oil in Kilograms: "))
def kg_gram(b):
    conversion=b*1000
    return conversion
print(kg_gram(b),"grams")
def kg_litre(b):
    conversion=b*1.1364
    return conversion
print(kg_litre(b),"litres")
g=float(input("Enter the time in hour: "))
def t_min(g):
    conversion=g*60
    return conversion
print(t_min(g),"minutes")
def t_sec(g):
    conversion=g*3600
    return conversion
print(t_sec(g),"seconds")

'''Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)'''

magnitude = float(input("Enter magnitude of Earthquake: "))
def Earthquake_Impact(magnitude):
    if magnitude<2:
        return "Micro Earthquake"
    elif 2<=magnitude<3:
        return "Very Minor Earthquake"
    elif 3<=magnitude<4:
        return "Minor Earthquake"
    elif 4<=magnitude<5:
        return "Light Earthquake"
    elif 5<=magnitude<6:
        return "Moderate Earthquake"
    elif 6<=magnitude<7:
        return "Strong Earthquake"
    elif 7<=magnitude<8:
        return "Major Earthquake"
    else:
        return "Great Earthquake"
print(Earthquake_Impact(magnitude))

'''Factor:  Calculate temperature that a person feels because of the wind (Python3)'''

a=float(input("Enter temperature in °C: "))
b=float(input("Enter wind speed in Km/h: "))
def temp_wind(a,b):
    output= 13.12 + 0.6215*a - 11.37*(b**0.16) + 0.3965*a(b**0.16) 
    return round(output,2)
print(temp_wind(a,b),"°C")

