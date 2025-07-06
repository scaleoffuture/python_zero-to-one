guests = ['Sonya', 'Timur', 'Pavel', 'Sasha', 'Vadim']
print(guests)

del guests[3]
guests.append('Daria')
print(guests) 

guests.insert(0, 'Asya')
guests.insert(3, 'Andrei')
guests.append('Elon')
print(guests)

message ="sorry we have a hassle. A new big dinner table won't arrive at time. So, I can invite only two people :( We'll meet next week in the best restaurant. \nI'll drop a line!"
Asya = guests.pop(0)
print(f'\n{Asya}, dear friend, {message}')
print(guests)

Vadim = guests.pop(4)
print(f'\n{Vadim}, dear friend, {message}')
print(guests)

Daria = guests.pop(4)
print(f'\n{Daria}, dear friend, {message}')
print(guests)