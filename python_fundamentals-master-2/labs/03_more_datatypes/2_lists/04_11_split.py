#'''
#Write a script that takes in a string from the user. Using the split() method,
#create a list of all the words in the string and print the word with the most
#occurrences.

#'''
# hallo wir sind hier versammelt und machen viele dinge und wiederholen uns immer wieder

from collections import counter
sentence = input("give some words here: ")
sentence = sentence.split()
sentence = str(sentence)


Counter = Counter(sentence)

most_occur = Counter.most_common(sentence)

print(most_occur)





print(s)
