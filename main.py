import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_alphabets = pandas.read_csv('nato_phonetic_alphabet.csv')
print(phonetic_alphabets)
phonetic_alphabets_dictionary = {row.letter:row.code for (index,row) in phonetic_alphabets.iterrows()}
print(phonetic_alphabets_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
print([phonetic_alphabets_dictionary[i.upper()] for i in word.strip()])