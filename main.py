
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
with open("./Input/Names/invited_names.txt") as name:
    name_list = name.readlines()

with open("./Input/Letters/starting_letter.txt") as text:
    main_text = text.read()
    for names in name_list:
        stripped_name = names.strip()
        read_text = main_text.replace("[name]", stripped_name)
        with open(f"Output/ReadyToSend/Letter_for_{stripped_name}.txt", "w") as letter:
            letter.write(read_text)
