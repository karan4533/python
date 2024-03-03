import random

def choose_word():
    words = ["hangman", "python", "programming", "computer", "game"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    max_attempts = 6
    word = choose_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts += 1
            print("Incorrect guess.")
            print(display_word(word, guessed_letters))
            print(f"Attempts remaining: {max_attempts - attempts}")

            if attempts == max_attempts:
                print("You've run out of attempts! The word was:", word)
                break
        else:
            print("Correct guess!")
            display = display_word(word, guessed_letters)
            print(display)

            if "_" not in display:
                print("Congratulations! You've guessed the word:", word)
                break

hangman()
