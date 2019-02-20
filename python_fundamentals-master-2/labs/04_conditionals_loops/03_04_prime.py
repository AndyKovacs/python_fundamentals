#'''
#Print out every prime number between 1 and 100.

#'''
#or x%3==0 or x%4==0 or x%5==0 or x%6==0 or x%7==0 or x%8==0 or x%9==0 or x%10==0:
#for x in range(1,100):
 #   if x%2==1 or x==1 and x%x==0:
  #      print(x)
   # elif x%3==1 and x%x==0:
    #    print(x)
    #else:
    #    print(x,False)
    #elif x%3==1:
     #   print(x)
    #elif x%4:
     #   print(x)
for number in range(1,100):
    zwei = 2
    while number > zwei:
        if number % zwei == 0:
            break
        else:
            zwei += 1
    if number == zwei:
        print(number)

