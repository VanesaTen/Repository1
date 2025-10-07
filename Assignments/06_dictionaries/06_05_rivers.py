# created dictionary with rivers

rivers = {'Nile River': 'Africa', 'Amazon River': 'South America', 'Yangtze River': 'China'}



# looped to print a sentence about each river

print("Sentence about each river:\n")
for key, value in rivers.items():
    print(f"{key} runs through {value}\n")

# loop to print name of rivers(keys)

print("Name of each river:\n")

for river in rivers.keys():
    print(river)

# loop to print nam of country(values)

print("\nName of each country:\n")
for country in rivers.values():
    print(country)
