'''Problem Statement- II
We have three categories to check. If the sum of divisors is greater than a number, the number is
abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
be perfect design control structure for this problem statement

#Nint=28 # Number to be validated 
#Div=1    #Divisor
#while Div<Nint:
#   if Nint % Div==0:
#        print(Div) # Suit1
#Div=Div+1  # Suit 2'''

n = 28
divisors_sum = 0
divisor = 1
while divisor < n:
    if n % divisor == 0:
        divisors_sum += divisor
    divisor += 1
if divisors_sum > n:
    print(f"{n} is abundant")
elif divisors_sum < n:
    print(f"{n} is deficient")
else:
    print(f"{n} is perfect")