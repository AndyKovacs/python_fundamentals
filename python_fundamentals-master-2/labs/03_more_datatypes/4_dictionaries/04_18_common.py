#'''
#Write a script that takes the following two dictionaries and creates a new dictionary by combining
#the common keys and adding the values of duplicate keys together. For example:
#
#_dict1 = {"a": 1, "b": 2, "c": 3}
#_dict2 = {"a": 2, "c": 4 , "d": 2}

#result = {"a": 3, "b": 2, "c": 7 , "d": 2}


#'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

for key in dict_2:
    if key in dict_1:
        dict_2[key] = dict_2[key] + dict_1[key]

dict_3 = {**dict_1, **dict_2}


print(dict_1)
print(dict_2)
print(dict_3)