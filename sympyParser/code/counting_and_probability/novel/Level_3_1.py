from sympy import symbols, simplify

# Define variables
total_letters = 26
letters_without_A = total_letters - 1  # 25 letters (B-Z)

# Calculate total number of 3-letter words
total_words = total_letters ** 3

# Calculate total number of 3-letter words without the letter A
words_without_A = letters_without_A ** 3

# Use complementary counting to find the number of words with at least one A
words_with_A = total_words - words_without_A

# Return the final answer
words_with_A
