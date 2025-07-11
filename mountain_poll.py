responses = {}

# Set a flag that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like to climb someday?")

    # Store the response in the dictionary.
    responses[name] = response
    
    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
    
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

