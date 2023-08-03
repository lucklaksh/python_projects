import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_alphabet)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the word please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()






