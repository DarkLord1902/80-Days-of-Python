# Importing Pandas
import pandas

# Read the data from nato_phonetic_alphabet csv file
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Make the dictionary in formatted way
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# Ask the user for word
input_word = input("Enter a word: ").upper()
# Search the word to word from dictionary for his alphabetical words
answer = [nato_dict[letter] for letter in input_word]
# Print the answer
print(answer)
