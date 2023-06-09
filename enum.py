names = ['peter parker', 'Clark Kent', 'Wade Wilson']
heroes = ['spiderman', 'Superman', 'Deadpool']

for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')