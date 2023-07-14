#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random
index = random.randint(0,len(word_list)-1)
letter = input("Guess the letter:\n").lower()
for l in word_list[index]:
    if(letter == l):
        print("Right")
    else:
        print("Wrong")
