#'''
#Write a script that "flattens" a list. For example:

#starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
#flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#'''

from itertools import chain
starting_list = [[1,2,3,4],[4,5],[7,8,9]]
print(itertools.chain([1,2,3,4],[4,5],[7,8,9]))


