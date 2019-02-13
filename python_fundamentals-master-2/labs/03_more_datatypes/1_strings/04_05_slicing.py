#'''

#Using string slicing, take in the user's name and print out their name translated to pig latin.
#For the purpose of this program, we will say that any word or name can be
#translated to pig latin by moving the first letter to the end, followed by "ay".

#For example: ryan -> yanray, caden -> adencay

#'''

s = input("enter your username: ")
first_letter = s[0]
rest_of_word = s[1:]
ending_ay = "ay"
latinform = first_letter+ending_ay

print (rest_of_word,latinform)