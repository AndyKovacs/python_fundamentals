'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results

numberinput = int(input("give number between 1 and 1000000000: "))
z =numberinput%4
y = numberinput%7
def func_4_and_7_divisible(z,y):

    if z == 0 and y==0:
        print("the number is divisible by 4 and 7")
        result = numberinput/4,numberinput/7
    return result

print(func_4_and_7_divisible(z,y))

