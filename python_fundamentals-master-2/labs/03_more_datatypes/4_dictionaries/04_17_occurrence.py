#'''
#Write a script that takes a string from the user and creates a dictionary of letter that exist
#in the string and the number of times they occur. For example:

#user_input = "hello"
#result = {"h": 1, "e": 1, "l": 2, "o": 1}

#'''
#for i in my_strings:
 #   my_dict= {strings.count(strings,i)}

strings = input("give some strings in: ")
my_strings =list(strings)


strings = dict()
for i in my_strings:
  strings[i] = strings.get(i, 0) + 1


print(strings)
