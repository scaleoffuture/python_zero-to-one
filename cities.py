# Using break to exit a loop.
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' to stop this program.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.upper()}.")