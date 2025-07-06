# There are two lists for the tests. The second one is specially empty.
bikes = ['redbull','honda', 'yamaha', 'ninja', 'suzuki' ]
bikes_2 = []

bikes[0] = 'fastline'
print(bikes)

bikes.append('flawless')
print(bikes)

bikes_2.append('redbull')
bikes_2.append('fastline')
bikes_2.append('flawless')
print(bikes_2)

bikes_2.insert(4, 'ninja')
bikes_2.insert(3, 'fruit')
print(bikes_2)

del bikes_2[3]
print(bikes_2)

owned = bikes_2.pop()
print(f'\nThe first motorcycle I owned was a {owned.title()}.')
print(bikes_2)

too_expensive = bikes_2.pop(0)
print(f'\nA {too_expensive.title()} is too expensive for her.')
print(bikes_2)

too_weak = 'fastline'
bikes_2.remove(too_weak)
print(f'\nA {too_weak.title()} is too weak for Captain America.')
print(bikes_2)



