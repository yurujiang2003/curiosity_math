from sympy import symbols, simplify

# Define the variables
total_letters = 26
letters_without_A = total_letters - 1  # 25 letters (B-Z)
word_length = 3

# Calculate total number of 3-letter words
total_words = total_letters ** word_length

# Calculate number of 3-letter words without the letter A
words_without_A = letters_without_A ** word_length

# Calculate the number of words with at least one A
words_with_at_least_one_A = total_words - words_without_A

# Return the final answer
words_with_at_least_one_A
