"""
This is a training program on how to create hangman program. It will consist of 5 programs
"""
    
#First program, a set of given word will be provided

word_list = ["ardvark","baboon","camel"]

#TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random
chosen_word = random.choice(word_list)

#TODO-2 Ask the user to guess a letter and assign their answer in variable called guess.Make guess a lower case
guess = input("Guess a letter : ").lower()#.lower syntax makes eventhough we insert capital the guess variable will always be assigned as lower case letter

#TODO-3 Check if the letter the user guessed is one of the letter from the chosen_word

for letter in chosen_word: #loop through all the letter in the chosen_word variable
    if letter == guess:
        print("Right")
    else:
        print("Wrong")