user_input =str(input("Write a word you want an acronym for: "))# get user input
phrase = user_input.split()# spllits the words so that they can be individual words
a = " "
for i in phrase:# runs through each word that was split
    a = a + str(i[0]).upper()# returns the first character of each word in capital letter

print(a)