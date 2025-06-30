import random

import hangman_project.hangman_word as hangman_word

from hangman_project.hangman_art import stages 

from hangman_project.hangman_art import logo 

print(logo[0])


lives = 6 

chosen_word = random.choice(hangman_word.word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range (word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)


game_over = False 
correct_letters = []



while not game_over:

    print(f"********************{lives}/6 LIVES LEFT********************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You have already guessed" , guess )


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter 
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1 
        print(f"You guessed {guess} , that's not in the word . You lose a life. " )
        if lives == 0:
            game_over = True
            print(f"********************IT WAS {chosen_word} You Lose********************")


    if "_" not in display:
        game_over = True
        print("********************You Win********************") 


    print(stages[lives])