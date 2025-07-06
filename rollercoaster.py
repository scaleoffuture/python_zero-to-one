# command 'int' converts a number into inputs.
height = input('How tall are you, in inches?')
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride. Let's go!")
else:
    print("\nYou'll be able to ride when you're a little older.")