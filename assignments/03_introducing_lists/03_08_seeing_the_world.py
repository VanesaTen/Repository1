Vacations = ['Paris', 'Hawaii', 'Rome','Italy']



print (Vacations[0])
print (Vacations[1])
print (Vacations[2])
print(Vacations[3])


#sorting the list
print("Here is the original list:")
print(Vacations)
print("\nHere is the sorted list:")
print(sorted(Vacations))
print("\nHere is the original list again:")
print(Vacations)

print ("\nThis is in reverse order:")
print(Vacations)
Vacations.reverse()
print(Vacations)

#reprint to reverse the list back
print(Vacations)
Vacations.reverse()
print(Vacations)

#storing list in alph order
Vacations.sort()
print(Vacations)


#storing lists in reverse alph order
Vacations.sort(reverse=True)
print(Vacations)

