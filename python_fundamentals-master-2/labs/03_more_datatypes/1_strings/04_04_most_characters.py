#'''
#Write a script that takes three strings from the user and prints the one with the most characters.

#'''

sentence_1 = input("please give three words,beginning with the first word: ")
sentence_2 = input("second word: ")
sentence_3 = input("third word: ")

sentence = [sentence_1,sentence_2,sentence_3]
sentence.sort(key=len,reverse=True)

print("the words will be sorted beginning with the word with the most characters",sentence)




