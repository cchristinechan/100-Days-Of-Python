#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_by_line = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    for name in names_list:
        stripped_name = name.strip()
        new_letter_with_name = letter_by_line.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as invite_letter:
            invite_letter.write(new_letter_with_name)
