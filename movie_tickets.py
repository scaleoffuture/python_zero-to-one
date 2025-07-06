text = '\nHow old are you?'
text += '\nWe have a special system of prices to get in our attraction depending on ages.'
# 0 because it is unknown for me how to combine numbers and words in one loop.
text += "\nIf you don't want to buy a ticket at all write '0'."

active = True
while active:
    message = input(text)
    message = int(message)

# The triple combo of 0 and 'active = False' for the solution 'no', 'No', 'NO' in the future.
    if message == 0:
        active = False
    elif message == 0:
        active = False
    elif message == 0:
        active = False
# The child can't say or write. Here's a problem.
    elif message == 1:
        print('Your ticket is free. Come in!')
    elif message == 2:
        print('Your ticket is free. Come in!')
    elif message < 12:
        print('Your ticket costs $10')
    elif message >= 12:
        print ('Your ticket costs $15')
        