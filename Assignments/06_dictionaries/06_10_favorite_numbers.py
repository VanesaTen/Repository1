# printing favorite numbers 

fav_nums = {'Rob': [6,9],'Joe': [8, 5 ],'Nelsa': [1,7], 'Jess': [9,3], 'Jaz': [2,9]}


print(fav_nums['Rob'])
print(fav_nums['Joe'])
print(fav_nums['Nelsa'])
print(fav_nums['Jess'])
print(fav_nums['Jaz'])

# for... printes all the values in the keys

for fav_num in fav_nums.keys():
    print(fav_num.title())