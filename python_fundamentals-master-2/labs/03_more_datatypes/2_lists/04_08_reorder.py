#'''
#Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
#Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
#Then print out the 9th, 7th, 5th, 3rd, and 1st.

#Example input: 1,2,3,4,5,6,7,8,9,10
#Example output: 2,4,6,8,10,9,7,5,3,1

#'''
#10 11 12 13 14 15 16 17 18 19
"""
numbs = [int(x) for x in input("give 10 numbers: ").split()]
numbs_2 = numbs[1]
numbs_4 = numbs[3]
numbs_6 = numbs[5]
numbs_8 = numbs[7]
numbs_10 = numbs[9]
numbs_gerade = [numbs_2,numbs_4,numbs_6,numbs_8,numbs_10]
numbs_1 = numbs[0]
numbs_3 = numbs[2]
numbs_5 = numbs[4]
numbs_7 = numbs[6]
numbs_9 = numbs[8]
numbs_ungerade =[numbs_1,numbs_3,numbs_5,numbs_7,numbs_9]
allesineinem =numbs_gerade+numbs_ungerade

print(allesineinem)
"""
list1=[]
list2=[]

y = input("Please give me 10 numbers seperated by commas: ")
y = y.replace(","," ")
y = y.split(" ")

for i in range(1,11,2):
    list1.append(y[i])


for i in range(-2,-11,-2):
    list2.append(y[i])
    finallist = list1 + list2

for element in finallist:
    print(element, end=" ")
