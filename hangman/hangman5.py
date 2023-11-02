
# This is a training program on how to create hangman program. It will consist of 5 programs  
#Fourth program
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
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
word_list = ["ardvark","baboon","camel"]
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#testing word
print(f"Pssttt...the chosen word is {chosen_word}")

lives = 6

display = [] #initialization
for _ in range(word_length): #determine how many underscore using the range which determined by the length of variable chosen_word
    display += '_'

while not end_of_game:

    guess = input("Guess a letter : ").lower()#.lower syntax makes eventhough we insert capital the guess variable will always be assigned as lower case letter
    
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    
    for position in range(word_length): 
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter
            
    
    if guess not in chosen_word:
       #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print ("you lose")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win")
    
    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
