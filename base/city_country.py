def city_country(city_name,country_name):
    full_name = f'{city_name},{country_name}'
    return full_name.title()
place = city_country('Rostov','Russia')
print(place)
place = city_country('Kiev','Ukraine')
print(place)
place = city_country('London','England')
print(place)