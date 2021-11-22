def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f'I am a {key} and I am a {val} belt')

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

ninja_intro(ninja_belts)