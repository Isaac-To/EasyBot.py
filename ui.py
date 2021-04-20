def num_list(list):
    for i, j in enumerate(list):
        print(i, j)
    
def sys_message(msg):
    msg = str(msg)
    length = 50
    length_side = round((length - len(msg))/2)
    for i in range(length_side):
        print('-', end='')
    print(msg, end='')
    for i in range(length_side):
        print('-', end='')
    print()