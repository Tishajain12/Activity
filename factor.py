#calculation of wind chill
T=float(input("enter temperature in fahrenheit: "))
W=float(input("enter wind speed: "))
print(35.74+0.6215*T-35.75*W**0.16+0.4275*T*W**0.16)