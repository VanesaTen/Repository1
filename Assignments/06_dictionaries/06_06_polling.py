favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'Jess': 'csharp',
    'Bob':'HTML'
    }

# people who should take the poll

polling_people = ['jen', 'sarah', 'rachel', 'mike', 'bob']

# loopin through the list of who should poll
for person in polling_people:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll!")
