alien_color = 'red'

if 'green' in alien_color:
    print("You just earned 5 points for shooting the alien!")
elif 'yellow' in alien_color:
    print("You just earned 10 points for shooting the alien!")
elif "red" in alien_color:
    print("You just earned 15 points for shooting the alien!")

#working with a dictionary.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print(f'\nThe alien is {alien_0['color']}.')
alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0["color"]}.')

alien_0['speed'] = 'fast'
print(f"\nOriginal position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# A list of dictionaries.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
alien_3 = {'color': 'midas gold', 'points': 50}

aliens = [alien_0, alien_1, alien_2, alien_3]
print(aliens)

# Make an empty list for storing aliens (power of range).
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Dynamic states of aliens
for alien in aliens[1:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien ['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

