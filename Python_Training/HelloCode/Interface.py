from random import randint
# Функции для создания интерфейса работы задач

# interface(enter program (input values), run program (choose Program), exit program)

def interface():
    while(True):
        choose_and_run()
        if (exit_prog('exit')): break
    exit()

def choose_and_run():
    while(True):
        run = choose_prog()
        choose_input_data()
        run_prog(run)
        if (exit_prog('repeat')): return

def choose_prog(): return enter_data('int', output_message('choose_p'))

def choose_input_data(set_list):
    return {
        'random': rnd_list,
        'enter': enter_list,
        'input': input_list,
        'default': default_list,
    }[set_list[0]](set_list)

def rnd_list(set_list: list):
    c = set_list[1]
    s = set_list[2]
    r = set_list[3]
    set_list.clear()
    for i in range(c):
        set_list.append(randint(s, r))
    return set_list

def default_list(set_list: list):
    set_list.clear()
    for i in range(10):
        set_list.append(randint(-100,101))
    return set_list

def exit_prog(message): return enter_data('bool', output_message(message))

def output_message(key):
    return {
        'choose_p': 'Enter Number of Program',
        'exit': 'Do you want to continue? y/n',
        'repeat': 'Repead program? y/n',
    }[key]

interface()