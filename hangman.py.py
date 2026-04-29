import random

def play_game():
    words = {
        "python": "Programming language",
        "apple": "A fruit",
        "table": "Furniture",
        "chair": "Used for sitting",
        "india": "A country"
    }

    stages = [
        """
         -----
         |   |
             |
             |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        --------
        """
    ]

    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed = ["_"] * len(word)
    guessed_letters = []
    attempts = 0
    max_attempts = 6

    print("\n" + "="*35)
    print("🎮 WELCOME TO HANGMAN GAME 🎮")
    print("="*35)
    print("Guess the word one letter at a time.")
    print("You have 6 chances to guess wrong.")
    print("Hint:", hint)

    while attempts < max_attempts and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Guessed letters:", ", ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        # ✅ Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter!")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("✅ Correct guess!")
        else:
            attempts += 1
            print("❌ Wrong guess!")
            print(stages[attempts])
            print(f"Remaining chances: {max_attempts - attempts}")

    # 🎯 Result
    print("\n" + "="*35)
    if "_" not in guessed:
        print("🎉 CONGRATULATIONS! YOU WON 🎉")
        print("The word was:", word.upper())
    else:
        print("💀 GAME OVER! YOU LOST 💀")
        print("The word was:", word.upper())
    print("="*35)


# 🔁 Replay option
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\n👋 Thank you for playing!")
        break