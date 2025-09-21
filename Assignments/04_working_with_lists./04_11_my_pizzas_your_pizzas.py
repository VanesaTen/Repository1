# printing two lists with different items in each list 

pizzas = ['sausage', 'mushroom','chicken',]
friend_pizzas = pizzas[:]


# adding items to different lists
pizzas.append('pepparoni\n')
friend_pizzas.append('onion\n')


# new list and comment 1
print(f'My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

# new list and comment 2
print(f'My friend’s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)


