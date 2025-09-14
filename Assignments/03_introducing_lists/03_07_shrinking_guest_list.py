
#Lists of items 

guests_list = ['John', 'Jessica', 'Suzuki', 'Mike']

guests_list.insert(0, 'Angie') #beginning
guests_list.insert(2, 'Maria') #middle
guests_list.append('Bobby') #end


message = f"Hello {guests_list[0]}, you are formally invited to dinner!"
print(message)

message = f"Hello {guests_list[1]}, you are formally invited to dinner!"
print(message)

message = f"Hello {guests_list[2]}, you are formally invited to dinner!" 
print(message)

message = f"Hello {guests_list[3]}, you are formally invited to dinner!"
print(message)

message = f"Hello {guests_list[4]}, you are formally invited to dinner!"
print(message)

message = f"Hello {guests_list[5]}, you are formally invited to dinner!"
print(message)

message = f"Hello {guests_list[6]}, you are formally invited to dinner!"
print(message)


print("We can only invite two people for dinner!")

#removing items using pop



message = f"Sorry {guests_list[5]}, you are not invited anymore!"
print(message)

popped_guests_list = guests_list.pop()
print(guests_list)
print(popped_guests_list)

message = f"Sorry {guests_list[4]}, you are not invited anymore!"
print(message)

popped_guests_list = guests_list.pop()
print(guests_list)
print(popped_guests_list)

message = f"Sorry {guests_list[3]}, you are not invited anymore!"
print(message)

popped_guests_list = guests_list.pop()
print(guests_list)
print(popped_guests_list)

message = f"Sorry {guests_list[2]}, you are not invited anymore!"
print(message)

popped_guests_list = guests_list.pop()
print(guests_list)
print(popped_guests_list)


message = f"Hello {guests_list[0]}, you are still invited to dinner!"
print(message)

message = f"Hello {guests_list[1]}, you are still invited to dinner!"
print(message)

# deleting from the list 

del guests_list[1]
del guests_list[0]

