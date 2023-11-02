
# This is a training program on how to create hangman program. It will consist of 5 programs  
#Second program

word_list = ["ardvark","baboon","camel"]

import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#testing word
print(f"Pssttt...the chosen word is {chosen_word}")

#TODO-1: Create an emmpty list called display
#for each letter in the chosen_word , add a "_" to 'display'

display = [] #initialization
for _ in range(word_length): #determine how many underscore using the range which determined by the length of variable chosen_word
    display += '_'
print(display)

guess = input("Guess a letter : ").lower()#.lower syntax makes eventhough we insert capital the guess variable will always be assigned as lower case letter

for position in range(word_length): 
    letter = chosen_word[position]
    if letter == guess:
        display[position]=letter
    else:
        display[position]='@'
print(display)
    
