import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
game_over = False
lives = len(stages) - 1

random_word = random.choice(word_list)
random_word_length = len(random_word)

display = []
for _ in range(random_word_length):
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for i in range(random_word_length):
        letter = random_word[i]
        if letter == guess:
            display[i] = letter
    print(f"{' '.join(display)}")

    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the random word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
            print(f"your word is {random_word}")

    if not "_" in display:
        game_over = True
        print("You win.")

    print(stages[lives])
