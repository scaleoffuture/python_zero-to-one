person = {'first_name': 'vlad', 'last_name': 'plitkin', 'favorite_number': "8", 'age': '19', 'city': 'podolsk'}

print(person)

person_2 = {'name': 'Vadim', 'favorite_number': "21"}
print(person_2)

person_3 = {'name': 'Mark', 'favorite_number': "1 000 000"}
print(person_3)

person_4 = {'name': 'Anton', 'favorite_number': "18 000"}
print(person_4)

person_5 = {'name': 'Iskander', 'favorite_number': "100"}
print(person_5)

people = [person, person_2, person_3, person_4, person_5]
print('\nHello friends!')
print('Here is all information about you:\n')

for person in people[:1]:
    print(people)
