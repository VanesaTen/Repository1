fav_places = {'Josh': ['Paris, Italy, France'], 'Sonia': ['Miami Cancun China'], 'Rudy': ['DisneyLand Area 51 Washington ']}


people = ['Josh', 'Sonia']  
for person in people:
    print(f"Hi, {person}, name your favorite places.")
print('....................')


for person in fav_places:
    print(f"{person}:{fav_places[person]}")
