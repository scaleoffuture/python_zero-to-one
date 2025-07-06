my_foods = ['pizza', 'falafel', 'carrot cake', 'rice', 'burgers', 'fries', 'cookies', 'ice cream', 'kfc']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

#Why can't I to add upper/lower/title commands after printing lists?
print('The first 3 items in the list are:')
print(my_foods[:3])
print('\n3 items from the middle of the list are:')
print(my_foods[3:6])
print("\nThe last 3 items in the list are:")
print(my_foods[-3:])

print("\nMy friend's favorite foods are:")
print(friend_foods)

#To show how copying lists work, I want to create another one.
my_meals = ["Vegatables", "Eggs", "Water"]
friend_meals = my_meals[:]

my_meals.append("Avokado")
friend_meals.append("Broccoli")

print("\nMy favorite meals are:")
print(my_meals)

print("\nMy friend's favorite meals are:")
print(friend_meals)

#And another one to show how works the equality in lists.
my_eats = ["Vegatables", "Eggs", "Water"]
friend_eats = my_eats

my_eats.append("Avokado")
friend_eats.append("Broccoli")

print("\nMy favorite eats are:")
print(my_eats)

print("\nMy friend's favorite eats are:")
print(friend_eats)