import random
words = ["apple", "banana", "grape", "orange", "mango"]
word = random.choice(words)
display = ["_"] * len(word)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print(" ".join(display))
while incorrect_guesses < max_guesses and "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = guess
        print("Good guess:", " ".join(display))
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! {max_guesses - incorrect_guesses} tries left.")
if "_" not in display:
    print("🎉 You win! The word was:", word)
else:
    print("💀 You lose! The word was:", word)
