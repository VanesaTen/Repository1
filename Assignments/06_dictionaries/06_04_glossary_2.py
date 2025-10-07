# adding five more keys and values


glossary = {'Dictionary':'Dictionary stores lists of variables.',
'Python': 'you are coding a program.','keyError': 'there is an error in keys.', 'Lists':
'there is a list of items','for_in': 'you can loop through items.', 
'output': 'displays the return', 'variables': 'its a box that stores data','string':'its a text',
'Boolean':'its true or false statements','integer': 'its a number without decimals' }


#this loops through it
for key, value in glossary.items():
    print(f"{key} means that {value}\n")
