#'''
#Take in the following three values from the user:
 #   - investment amount
  #  - interest rate in percentage
   # - number of years to invest

#Print the future values to the console.

#'''
a=input("please give the number of the investment amount: ")
b=input("please give the interest rate in percentage: ")
c=input("please give the number of years of interest: ")

a=int(a)
b=int(b)
c=int(c)

d = a*(1+b*0.01)**c

print ("Your future value is",d)