
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
with open("./Input/Names/invited_names.txt") as name:
    name_list = []
    for line in name.readlines():
        name_list.append(line.strip())


with open("./Input/Letters/starting_letter.txt") as text:
    main_text = text.read()
    for names in name_list:
        read_text = main_text.replace("[name]", names)
        with open(f"Output/ReadyToSend/Letter_for_{names}.txt", "w") as letter:
            letter.write(read_text)
