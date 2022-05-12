word = "building"

guess_letter = ""
while guess_letter != "?":
    guess_letter = input("Please type a letter (or ? to quit): ")
    guess_letter = guess_letter.lower()

    if guess_letter in word:
        print(f"The word contains the letter {guess_letter}")
    else:
        print(f"The letter {guess_letter} is not found in the word.")

    for letter in word:
        if letter.lower() == guess_letter:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")

    print()