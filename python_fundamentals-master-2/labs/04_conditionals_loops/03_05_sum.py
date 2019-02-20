#'''
#Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
#	of numbers from the lower bound to the upper bound.
#
#	For example, if a user enters 1 and 100, the output should be:
#		The sum is: 5050
#'''

number1=int(input("give the first number in: "))
number2=int(input("give the second number: "))
my_sum = 0
for numbs in range(number1,number2+1):
    my_sum += numbs


print(my_sum)


   # else:
    #   print(number1)
    #number1+=1

#for numbs in range(1,10):
 #   print (numbs)
