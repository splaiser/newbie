river = {'egypt': 'nile', 'russia' : 'amur','england' : 'sena'}
for key,value in river.items():
    print(f"The {value.title()} runs through {key.title()} ")

print("Rivers:")
for rivers in river.values():
    print(rivers.title())
print("Countries:")
for country in river.keys():
    print(country.title())
