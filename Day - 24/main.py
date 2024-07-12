# Open the invited names file
with open("./Names/invited_names.txt") as invited_names:
    # Make the list of invited names from that file
    names_list = (invited_names.readlines())

# Open the starting letters file
with open("./Letters/starting_letter.txt") as file:
    # Read the file at once
    contents = file.read()

    # Make the for loop to get the names from names_list
    for name in names_list:
        # strip the one by one name
        name = name.strip()
        # Replace the content from letters with name
        new = contents.replace("[name]", name)
        # Crate a new file for output and add all the outputs to that file
        with open(f"./Outputs/letter_for_{name}.txt", mode="w") as final_file:
            # Update all the input and generate output
            final_file.write(new)
