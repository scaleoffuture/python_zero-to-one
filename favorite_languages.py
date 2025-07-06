favorite_languages = {

'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python'

}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

# Keys or Values in looping a dictionary?
print("They're exactly in our list related to lovely languages:")
for name in favorite_languages.keys():
    print(name.title())

print("\nThe following languages have been mentioned:")
for output in favorite_languages.values():
    print(output.upper())

# An additional hard task
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"\nHi {name.title()}.")

    if name in friends: 
        language = favorite_languages.keys()
        print(f"\t{name.title()}, I see you love {language}!")

# Looping through a dictionary's keys in a particular order.
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# A set command for unique items in the output.
print("\nThe following languages have been mentioned:")
for language in set (favorite_languages.values()):
    print(language.title())

