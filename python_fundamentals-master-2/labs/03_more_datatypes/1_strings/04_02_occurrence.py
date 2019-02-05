#'''
#Write a script that takes a string of words and a letter from the user.
#Find the index of first occurrence of the letter in the string. For example:

#String input: hello world
#Letter input:
#Result: 4

#'''

sentence = input ("give some words here: ")
letter = input ( "choose a letter: ")
sentence = str(sentence)
letter = str (letter)
letterfind =len(sentence)
ausdruck = "the result is"

print (ausdruck,(sentence.find(letter)))