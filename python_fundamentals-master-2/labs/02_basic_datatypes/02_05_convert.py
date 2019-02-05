#'''

#Demonstrate how to:

 #   1) Convert an int to a float
  #  2) Convert a float to an int
   # 3) Perform floor division using a float and an int.
    #4) Use two user inputted values to perform multiplication.

    #Take note of what information is lost when some conversions take place.

#'''
x=5         #first task
x=float(5)
print (x)

y=2.0
y=int(2.0)
print (y)

print (x//y)
z = (input ("Please select the first number,that should be multiplied: "))
w = (input ("please select the seond number, that should multiplied with the first number"))
z = int(z)
w = int(w)
print ("result is",z*w)