favorit_places = {
    'nikita': ['sea','mountains','city'],
    'sveta': ['sea','beach','mountains'],
    'katya': ['city','home_city','natures']
}
for name,places in favorit_places.items():
    print(f'{name.title()}s favorite place is :' )
    for place in places:
        print(f"\t{place.title()}")
