
# This is a training program on how to create hangman program. It will consist of 5 programs  
#Third program

word_list = ["ardvark","baboon","camel"]

import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#testing word
print(f"Pssttt...the chosen word is {chosen_word}")

#TODO-1: use a while loop to let the user guess again. the loop should only stop once the user has guessed all the letter in chosen word and display has no more blanks.
#then you can tell the user has won

display = [] #initialization
for _ in range(word_length): #determine how many underscore using the range which determined by the length of variable chosen_word
    display += '_'
print(display)

end_of_game = False

while not end_of_game:

    guess = input("Guess a letter : ").lower()#.lower syntax makes eventhough we insert capital the guess variable will always be assigned as lower case letter

    for position in range(word_length): 
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You won")
    
