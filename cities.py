cities = {
    'rostov-on-don': {
        'country' : 'russia',
        'population' : '1.1 million',
        'fact' : 'My home-city, where im born'
    },
    'london': {
        'country' : 'england',
        'population' : '8.9 million',
        'fact' : 'Bigest city in england'
    },
    'rafaelkovka':{
        'country' : 'ukraine',
        'population' : '1117',
        'fact' : 'City where katya born'
    }
}
for city_name,city_info in cities.items():
    print(f"\nCity: {city_name.title()}")
    print(f"Countries where place is {city_info['country']}")
    print(f"{city_info['population']} peoples lives in this city")
    print(f"{city_info['fact']}. Do you now that information?")