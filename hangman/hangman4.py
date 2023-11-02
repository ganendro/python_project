
# This is a training program on how to create hangman program. It will consist of 5 programs  
#Third program
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark","baboon","camel"]
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#testing word
print(f"Pssttt...the chosen word is {chosen_word}")

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives = 6

display = [] #initialization
for _ in range(word_length): #determine how many underscore using the range which determined by the length of variable chosen_word
    display += '_'

while not end_of_game:

    guess = input("Guess a letter : ").lower()#.lower syntax makes eventhough we insert capital the guess variable will always be assigned as lower case letter

    for position in range(word_length): 
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter
            
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print ("you lose")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win")
    
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
