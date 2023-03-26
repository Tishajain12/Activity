'''Tour Expenditure at Given Hotel 

The family has spent the vacation in Goa and now they are returning home to do so they will have to check out from the hotel.

Tariff on Room: Delux Room- 7500 INR

                            Non AC Room- 4500 INR 

You  as a developer has to create a program for a hotel owner which has the following requirements,

The program should begin with taking input from the checkout counter 

Type of room booked 
Total number of days 
Total Amount on Food (Amount is expected )
There are the following cases to be considered while generating a bill.

The tax on food amount is dependent on the type of room booked.

Tax on food for the deluxe room will be billed  18% of the total food amount.

Tax on food for the Non AC room will be billed  5% of the total food amount.

You are supposed to include a tip of 10% on the food amount.

The output from your program should include;

The  Room Tariff on the number of days spend, GST on a meal(Breakdown of GST is necessary based on CGST and SGST and same has to get reflected on console ) 

The tip amount, and the grand total for the meal including both the tax and the tip.

Format the output so that all of the values are displayed using two decimal places.'''

 
a=int(input("1.Deluxe, 2.Non-AC: "))
b=int(input("Enter number of days you have stayed:  "))  
c=float(input("Enter the total amount you have paid for food:  "))

if a == 1:
    charge= 7500 * b
    tax=0.18*c
else:
    charge = 4500*b
    tax=0.05*c
tip=0.1*c
total= charge+tip+tax+c
print(f"tip amount {tip} rupees")
print(f"food amount breaks CGST: {0.5*tax}  SGST: {0.5*tax} rupees")
print(f"grand total: {total} rupees")