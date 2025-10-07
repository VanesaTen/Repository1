# my three dictionaries 
person_1 = {'First_name':'Joe','Last_name': 'Smith','age' : 45,'city': 'Reading'}
person_2 = {'First_name':'Manny','Last_name': 'Esquivel','age' : 35,'city': 'Allentown'}
person_3 = {'First_name':'Ricardo','Last_name': 'Ventura','age' : 15,'city': 'Limerick'}

# combining all three lists 
people_list = [person_1, person_2, person_3]


# looping through  the list
for person in people_list:


    print(person['First_name'])
    print(person['Last_name'])
    print(person['age'])
    print(person['city'])
    print('................')