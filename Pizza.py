database = dict()
for i_count in range(int(input('Введите количество заказов: '))):
    order = input(f'{i_count + 1}-й заказ: ').split()
    if order[0] in database:
        if order[1] in database[order[0]]:
            database[order[0]][order[1]] += int(order[2])
        else:
            database[order[0]][order[1]] = order[2]
    else:
        database[order[0]] = dict({order[1]: int(order[2])})

for elem1 in sorted(database):
    print(f'\n{elem1}: ')
    for elem2 in sorted(database[elem1]):
        print(f'\t{elem2}: {database[elem1][elem2]}')
