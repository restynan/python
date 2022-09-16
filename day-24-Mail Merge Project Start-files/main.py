PLACEHOLDER = "[name]"
# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

# Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

    for name in names:
        stripped_name = name.strip()
        print(stripped_name)
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        #print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)


