def num_list(list):
    for i, j in enumerate(list):
        print(i, j)

def list_dict(dict):
    for key, value in dict.items():
        print(f'{key} | {value}')

def sys_message(msg):
    msg = str(msg)
    length = 50
    length_side = round((length - len(msg))/2)
    print()
    for i in range(length_side):
        print('-', end='')
    print(msg, end='')
    for i in range(length_side):
        print('-', end='')
    print()

def clear():
    from os import system
    system("cls")