message = input("Tell me something, and I will repeat it back to you:")
print(message)

prompt = "If you share youe name, we can personalize the message you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f'Hello, {name}!')

# Defining a function.

def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()