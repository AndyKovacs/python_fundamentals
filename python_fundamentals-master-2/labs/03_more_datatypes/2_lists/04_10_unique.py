#'''
#Write a script that creates a list of all unique values in a list. For example:

#list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
#unique_list = [55, 'hi', 4, 13]


#'''

liste = [1,2,6,55,2,'hi',4,6,1,13]
setlist1 = set(liste)
setlist2 = list(liste)
new_list= liste-setlist2


print(new_list)