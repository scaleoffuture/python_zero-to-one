# Letting the user choose when to quit.
prompt = '\nTell me something, and I will repeat it back to you!'
prompt += "\nEnter 'quit' to end the program."

message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

# Using a flag. the same program. don't use them in parallel.
prompt = '\nTell me something, and I will repeat it back to you!'
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

if message == 'quit':
    active == False
else:
    print(message)
