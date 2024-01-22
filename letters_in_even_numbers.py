# Create a program that will --

# Accept a string from the user and display characters that are present at an even index number.

# DEADLINE: JANUARY 26, 2024

# Expected results
# Orginal String is pynative
# Printing only even index chars
# p
# n
# t
# v

# pseudocode
# Adding an input function so that it can accept a string from the user
word_given = str(input("Enter your word: "))
print(word_given)

# Length of the word
length = len(word_given)

# adding a loop
print("Printing only even index:")
for letters in range(0, length- 1, 2):
    print(length[letters])