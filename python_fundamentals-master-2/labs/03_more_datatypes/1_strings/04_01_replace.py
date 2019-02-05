#'''
#Write a script that takes a string of words and a symbol from the user.
#Replace all occurrences of the first letter with the symbol. For example:

#String input: more python programming please
#Symbol input: #
#Result: #ore python progra##ing please

#'''

words = input("please give some words or one sentence: ")
symbol = input ("please give a symbol here: ")
ersatz = words[0]

print(words.replace(words,symbol))



