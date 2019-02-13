#'''
#Write a script that sorts a dictionary into a list of tuples based on values. For example:

#input_dict = {"item1": 5, "item2": 6, "item3": 1}
#result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

#'''

from operator import itemgetter

dict_1={"item1":5,"item2":6,"item3":1,"item5":8,"item4":9}
list_1=list(dict_1.items())


list_2=sorted(list_1, key=lambda x: x[1])


print(list_2)