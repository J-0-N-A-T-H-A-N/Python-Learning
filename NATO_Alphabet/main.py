
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate():
    word = input("What word would you like translated? ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Make sure you are only entering letters\n")
        generate()
    else:
        print(phonetic_list)

generate()