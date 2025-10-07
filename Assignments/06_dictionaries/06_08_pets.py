# dictionary about pet info

dogs = {'breed': 'pitbull', 'owner': 'Mike', 'age': 2,}

cats = {'breed': 'ragdoll', 'owner': 'Jessica',  'age': 5}

birds = {'breed': 'parrot','owner': 'Ruby', 'age': 105}

pets = [dogs, cats, birds]

for pet in pets:

    print(f"Breed: {pet['breed']}")
    print(f"Owner: {pet['owner']}")
    print(f"Age: {pet['age']}")
    print('....................')