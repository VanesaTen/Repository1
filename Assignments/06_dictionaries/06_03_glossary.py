# printing key value pairs

glossary = {'Dictionary':'Dictionary stores lists of variables.','Python': 'your coding in a language.','keyError': 'there is an error in the program.', 'lists': 'there is a list of elements in a dictionary','for_in': 'you can loop through items.'}

# this loops through it
for key, value in glossary.items():
    print(f"{key} means that {value}\n")

