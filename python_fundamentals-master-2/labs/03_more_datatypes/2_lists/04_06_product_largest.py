#'''
#Take in 10 numbers from the user. Place the numbers in a list.
#Calculate the product of all of the numbers in the list.
#Also, find the largest number in the list.

#Print the results.

#'''

#sentence = input("give 10 numbers by putting a comma between the numbers: ")

from functools import reduce
sentence = [int(x) for x in input("give 10 numbers: ").split()]
produkt = reduce((lambda x, y: x * y), sentence)
print(produkt)