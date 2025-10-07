# printing favorite numbers 


fav_num = {'Rob': 6 ,'Joe': 8, 'Nelsa': 1,'Jess': 9, 'Jaz': 2}


print(fav_num['Rob'])
print(fav_num['Joe'])
print(fav_num['Nelsa'])
print(fav_num['Jess'])
print(fav_num['Jaz'])

for name in fav_num.keys():
    print(name.title())