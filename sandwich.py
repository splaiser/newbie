sandwich_orders = ['peperony sandwich','pastrami','red fish sandwich','pastrami','cheese sandwich']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        print(f'sorry but pastrami is ended')
        sandwich_orders.remove('pastrami')
        continue
    print(f'im start make your {sandwich.title()}')
    finished_sandwiches.append(sandwich)
print(f'All your sandwiches finished:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
