# There are two equal lists for testing, because I don't understand how to return an original version of the list after sorting.
cars = ['bmw', 'tesla', 'apple', 'china', 'rr']
cars_2 = ['bmw', 'tesla', 'apple', 'china', 'rr'] 

print(cars)
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("\nHere is the original list:")
print(cars_2)
print('Here is the sorted list:')
print(sorted(cars_2))
print('Here is the original one again:')
print(cars_2)
#I've got how to return the original list again due using the command 'print(sorted(+a list's name))'

cars_2.reverse()
print(cars_2)
len(cars)
len(cars_2)
#Lenghts can't be used?

#testing if else
for car in cars: 
    if car == 'bmw':
        print(car.upper())
    else:
        print (car.title())  

#conditional tests
supercar = 'subaru'
print("Is supercar == 'subaru'? I predict False")
print(supercar != 'subaru')

fastcar = 'formula'
print("\nIs fastcar == 'formula'? I predict True")
print(fastcar == 'formula')

electro = "e-tron"
print("\nIs electro == 'e-tron'? I predict False")
print(electro == 'tesla')

benz = 'benz'
print("\nIs benz == 'benz'? I predict True")
print(benz == 'benz')

speedycar = "tayota"
print('\nIs speedycar == "tayota"? I predict False')
print(speedycar == 'Lightning McQueen')
