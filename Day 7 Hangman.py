
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in range (len(chosen_word)):
  display.append('_')

while not end_of_game:
    guess = input("Guess a letter: ").lower()
  
    if guess in display:
      print(f"You have already guessed {guess}. Try again")
   
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
   
    if guess not in chosen_word:
        print(f"You've guessed {guess}. This letter is not in the word. You have lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was ''{chosen_word}''")
   
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])