sandwich_orders = ['cheese', 'chicken', 'potato']
finished_sandwiches = []

while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print (f'Preparing your orders! It takes 3 mins! {preparing_sandwich.title()}')
    finished_sandwiches.append(preparing_sandwich)

print("\nThe following sandwiched were prepared specially for you. Enjoy!")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())