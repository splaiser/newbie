tables = input("How many seats you are need?")
tables = int(tables)
if tables > 8:
    print(f'We havent table with {tables} seats now.We need times for search it for you')
else:
    print(f'Table with {tables} seats already! Follow me!')