favorite_places = {
    'luke': 'the star park',
    'anya': 'just park',
    'tony': 'the lab',
    'pepper': 'stark industries',

}

for name in favorite_places.keys():
    print(f"It's {name.title()}.")

print("\n\tNice to meet you!\n")

for place in favorite_places.values():
    print(f"He/she really likes this place - {place.title()}")
