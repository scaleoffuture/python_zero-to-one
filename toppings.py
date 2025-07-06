#testing conditional
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#testing multiple conditions - a series of independent if statements
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print('Finished making your pizza!\n')

#if statements with lists more
requested_toppies = ['mushrooms', 'green peppers', 'french fries', 'extra cheese']
for requested_toppie in requested_toppies:
    print(f'Adding {requested_toppie}.')
print('Finished making your pizza!\n')

for requested_toppie in requested_toppies:
    if requested_toppie == "green peppers":
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f"Adding {requested_toppie}.")
print('Finished making your pizza!\n')

#checking an empty list
requested_topps = []

if requested_topps:
    for requested_topp in requested_topps:
        print(f"Adding {requested_topp}.")
        print('Finished making your pizza!\n')
#use if-else in the same lines. Otherwise, code will not be activated.
else:
        print('Sorry, we are out of toppings. We can suggest you a free royal dessert!\n')

#using multiple lists
available_toppies = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

for requested_toppie in requested_toppies:
    if requested_toppie in available_toppies:
        print(f'Adding {requested_toppie}.')
    else:
        print(f'Sorry, we do not have {requested_toppie}.')
print('Finished making your pizza!\n')

    

