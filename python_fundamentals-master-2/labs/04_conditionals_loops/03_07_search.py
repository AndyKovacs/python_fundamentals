'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

receive = int(input("select a number between 0 and 1000000000: "))
my_guess = 0
while my_guess < 1000000000:
    if my_guess !=receive:
        my_guess += 1
    elif my_guess==receive:
        print("your number is "+str(my_guess))
        break


