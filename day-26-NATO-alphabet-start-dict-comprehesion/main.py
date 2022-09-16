import pandas
nato_phonetic_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato_phonetic_data_frame)
nato_phonetic_dict = {row.letter: row.code for (key, row) in nato_phonetic_data_frame.iterrows()}
print(nato_phonetic_dict)

user_input = input("Enter a word: ").upper()
out_put = []
out_put = [nato_phonetic_dict[letter] for letter in user_input]
print(out_put)



