#!/usr/bin/python3

hrs=int(input("Enter Hours\n"))
rate=float(input("Enter  rate per hours\n"))

if (hrs > 40):
    salary=40*rate
    salary+=((hrs-40)*(rate*1.5))
else:
    salary=hrs*rate

print ("Gross salary = %f" %salary)
    
