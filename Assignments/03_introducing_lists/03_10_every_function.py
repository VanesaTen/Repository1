phones = ['samsung', 'iphone', 'oneplus']


print (phones[0])
print (phones[1])
print (phones[2])

#personalized message 
print(f"Should I purchase a {phones[0]}?")

print(f"Should I purchase a {phones[1]}?")

print(f"Should I purchase a {phones[2]}?")


#printing in different order

message = f"\nI would like to own a {phones[0].title()}."
print (message)

message = f"I own a {phones[2].title()}."
print(message)

message = f"I would prefer to own a {phones[1].title()}."
print (message)

# Modifying the list

phones [1] = 'motorola'

message = f"\nI would like to own a {phones[0].title()}."
print (message)

message = f"I own a {phones[2].title()}."
print(message)

message = f"I would prefer to own a {phones[1].title()}.\n"
print (message)

#adding new phones to the list & printing the list of all phones

phones.insert(0, 'z flip') #beginning
phones.insert(2, 'z fold') #middle
phones.append('Google 10 pro') #end

print (phones[0])
print (phones[1])
print (phones[2])
print (phones[3])
print (phones[4])
print (phones[5])

# removing items using pop

message = f"\nThe {phones[5]} has loow quality. Crossing off my list!"
print(message)

popped_phones = phones.pop()
print(phones)
print(popped_phones)



message = f"\nThe {phones[4]} battery drains fast. Crossing off my list!"
print(message)

popped_phones = phones.pop()
print(phones)
print(popped_phones)


message = f"\nThe {phones[3]} features are limited. Crossing off my list!"
print(message)

popped_phones = phones.pop()
print(phones)
print(popped_phones)

'''
# deleting from the list 
del phones[2]
del phones[1]
del phones[0]
'''
'''
#sorting the list
print("Here is the original list:")
print(phones)
print("\nHere is the sorted list:")
print(sorted(phones))
print("\nHere is the original list again:")
print(phones)
'''

'''
#In reverse order
print ("\nThis is in reverse order:")
print(phones)
phones.reverse()
print(phones)
'''

'''
#reprint to reverse the list back
print(phones)
phones.reverse()
print(phones)
'''

'''
#storing list in alph order
phones.sort()
print(phones)
'''

'''
#storing lists in reverse alph order
phones.sort(reverse=True)
print(phones)
'''
print(len(phones))
