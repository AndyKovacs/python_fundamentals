#'''
#Write a program that takes a number between 1 and 1,000,000,000
#from the user and determines whether it is divisible by 3 using an if statement.
#Print the result.

#'''

number=int(input("give a number between 1 and 100.000.000: "))


if number %3 == 0:
    rightnumber=number/3
    print("the result is",rightnumber,"the number is divisvle by 3")

else:
    wrongnumber=number/3
    print("the result is",wrongnumber,"the number is not divisble by 3")

