# if elif else chain
age = 5
if age < 6:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
elif age < 65:
    print("Your admission cost is $40.")
else:
    print("Your admission cost is $20.")

#more comfortable 'print'
age = 12
if age < 6:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"\nYour admission cost is ${price}.")

#without 'else'
age = 70
if age < 6:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"\nYour admission cost is ${price}.")