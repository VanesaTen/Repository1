#guest list for dinner

guests_list = ['John', 'Jessica', 'Suzuki', 'Mike']


message = f"Hello {guests_list[0].title()}, you are formally invited to dinner!"
print(message)

message = f"Hello {guests_list[1].title()}, you are formally invited to dinner!"
print(message)

message = f"Hello {guests_list[2].title()}, you are formally invited to dinner!" 
print(message)

message = f"Hello {guests_list[3].title()}, you are formally invited to dinner!"
print(message)

# change of plans. One guest can't make it
message = f"Unfortunately, {guests_list[1].title()} can't make it to dinner."
print(message)

# Modifying the list

guests_list [1] = 'Susan'

#new invitations

message = f"Hello {guests_list[0].title()}, you are formally invited to dinner!"
print(message)

message = f"Hello {guests_list[1].title()}, you are formally invited to dinner!"
print(message)

message = f"Hello {guests_list[2].title()}, you are formally invited to dinner!" 
print(message)

message = f"Hello {guests_list[3].title()}, you are formally invited to dinner!"
print(message)

