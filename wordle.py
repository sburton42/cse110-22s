# Print a welcome message

# Make a variable for the secret word (and assign it the word for them to guess)
secret_word = "building"

# Print the hint (based on the secret word)
## This isn't a real hint that checks for matches or anything, this one is simply
## Go through the letters in the word and print an underscore for each one


# Ask the user for their guess
guess = input("What is your guess? ")

# Make a variable to keep track of the number of guesses and start it at 0 (or 1?)

# Do the following, as long as the users guessed word is not equal to the secret word
while guess != secret_word:
    # Add one to the number of guesses (for example x = x + 1)

    # Show them the hint

    # Go through each letter in guess
    # We could do: "for letter in guess", but then we woudln't know the i...
    # Instead try:
    for i, letter in enumerate(guess):
        # Now, we have both the letter and the i...
        # Check if the letter is in the secret word at all (hint: if letter in ...)
            # Find out if it's in the right place (hint: if letter == secret_word[i]...)
                # If so, print out the capital version
                # If not in the right place (but still in the word), print out the lower case
        # It was was not in the word at all, then print out an underscore

    # Ask for another guess
    guess = input("What is your guess? ")

# Print a message to tell them they guessed it
print("Congratulations! You guessed it!")

# Print out the number of guesses it took...