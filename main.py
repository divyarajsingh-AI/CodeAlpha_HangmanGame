import random

# Predefined list of words
words = ["python", "hangman", "codealpha", "program", "developer"]
word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(word_to_guess))  # Show blanks

while attempts_left > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
    else:
        attempts_left -= 1
        print(f"❌ Wrong! You have {attempts_left} attempts left.")

    # Show current word state
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check win condition
    if all(letter in guessed_letters for letter in word_to_guess):
        print("🎉 You guessed the word correctly!")
        break
else:
    print(f"😢 You lost! The word was: {word_to_guess}")
