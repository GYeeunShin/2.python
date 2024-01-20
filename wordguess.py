import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "grape", "lemon", "orange", "strawberry", "watermelon"]

# Function to choose a random word from the list
def choose_random_word():
    return random.choice(word_list)

# Function to play the game
def play_game(word):
    guessed_word = ['_'] * len(word)
    attempts = 6  # You can change the number of attempts

    print("Welcome to the Word Guess Game!")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print(" ".join(guessed_word))
            if "_" not in guessed_word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

    if attempts == 0:
        print("Sorry, you're out of attempts. The word was:", word)

# Main game loop
while True:
    word_to_guess = choose_random_word()
    play_game(word_to_guess)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
