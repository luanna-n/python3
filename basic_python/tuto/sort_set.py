def belt_count(dictionary):
    #recebe os valores do dict e armazena numa lista
    belts = list(dictionary.values())
    #loops through the list
    #preciso transformar belts em um set para eliminar a duplicação no output
    for belt in set(belts):
        #conte quantas vezes um certo belt aparece em belts
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

ninja_belts = {}

while True:
    ninja_name = input('enter ninja name: ')
    ninja_belt = input('enter ninja belt: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? y/n: ')
    if another == 'y':
        continue
    else:
        break

belt_count(ninja_belts)