# A Dictionary in a Dictionary
# still in the process of rechanging...
# the quotes' problem.
users = {
    'aeinstein': {
        "first": 'albert',
        "last": 'einstein',
        "location": 'princeton',
        "quote": 'Strive not to be a success, but rather to be of value.',
    },
    'mcurie': {
        "first": 'marie',
        "last": 'curie',
        "location": 'paris',
        "quote": 'Be less curious about people and more curious about ideas.',},

        'bfranklin': {
            "first": 'ben',
            "last": 'franklin',
            "location": 'philadelphia',
            "quote": 'Blessed is he that expects nothing, for he shall never be disappointed.'},
        
        

        'pdurov': {
            "first": "pavel",
            "last": "durov",
            "location": "paris",
            "quote": "Не бойтесь делать то, что вы считаете правильным, даже если это противоречит мнению большинства."
        }    

    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    quote = ['quote']

    print(f'\tFull name: {full_name.title()}')
    print(f'\tLocation: {location.title()}')