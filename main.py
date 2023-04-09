
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
with open("./Input/Names/invited_names.txt") as name:
    name_list = []
    for line in name.readlines():
        name_list.append(line.strip())

for names in name_list:
    with open("./Input/Letters/starting_letter.txt") as text:
        main_text = text.read()
    main_text = main_text.replace("[name]", names)
    #print(main_text)
    with open(f"Output/ReadyToSend/Letter_for_{names}.txt", "w") as letter:
        letter.write(main_text)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
