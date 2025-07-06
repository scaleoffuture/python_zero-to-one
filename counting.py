current_number = 1
while current_number <= 5:
    print(current_number)
    # The += operator is equivelent to 'current_number = current_number + 1'.
    current_number += 1

# Using continue in a loop.
new_current_number = 0
while new_current_number < 10:
    new_current_number += 1
    if new_current_number % 2 == 0:
        continue
    print(new_current_number)

# Avoiding infinite loops.

x = 1
while x <= 5:
    print(x)
    x += 1