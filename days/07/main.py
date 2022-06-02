# Hangman Project
import random
import hangman_art
from hangman_words import word_list


def has_blanks(word):
    return "_" in word


lives = 6

stages = hangman_art.stages

chosen_word = random.choice(word_list)

print(hangman_art.logo)

display = []
for _ in chosen_word:
    display.append("_")

secret_word = " ".join(display)

print(f"Your word is {secret_word}")

while has_blanks(display) and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word.")
        lives -= 1
    elif guess in display:
        print(f"You already guessed letter {guess}.")

    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess

    print(" ".join(display))

    print(stages[lives])

    if not has_blanks(display) and lives > 0:
        print("You win!!!")
    elif lives == 0:
        print("You lose :(")
