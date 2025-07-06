# The += operator is equivelent to 'prompt = prompt + 1'.
prompt = '\nPlease choose your topping.'
prompt += "\nYou'll add that topping to your pizza. You can add as much as you want. We have any of them."
prompt += "\n(Write 'no' if you don't want any topping)."

while True:
    topping = input(prompt)

    if topping == 'no':
        break
    elif topping == 'No':
        break
    elif topping == 'NO':
        break
    else:
        print('Such a nice choice!')
    
