#'''
#Write a script that takes a string from the user and creates a list of tuples with each word.
#For example:

#input = "hello world"
#result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

#'''


one_tuple_1 = input("give one string here: ")
one_tuple_2 = input("give one more string here: ")
one_tuple_1 = tuple(one_tuple_1)
one_tuple_2 = tuple(one_tuple_2)
#sum_list = zip(one_tuple_1,one_tuple_2)

my_list = [one_tuple_1,one_tuple_2]

print(my_list)

