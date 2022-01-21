# Вводные функции

def input_data(set_up_list):
    for i in range(1, len(set_up_list)):
        while True:
            new_data = check_input_data(input(f'{set_up_list[i]}: '))
            if type(new_data) == type(set_up_list[0]):
                break
    return new_data

def check_input_data(data):
    try:
        input_type = int(data)
    except ValueError:
        try:
            input_type = float(data)
        except ValueError:
            try:
                input_type = str(data)
            except ValueError:
                print('Unindentify type')
    return input_type

def call_program(task, value_list):
    print(task)
    call = {
        23: degree_n,
        25: sum_cow,
        27: count_numeric_in_number,
    }
    print(call[task](value_list))

def interface(number_of_task):
    
    # formats_of_data = {
    #     'int' : 1,
    #     'float' : 1.1,
    #     'str': 'str'
    # }
    
    # for x in formats_of_data:
    #     for i in task_start_list:
    #         task_start_list[i][0] = formats_of_data[x]
    # print(task_start_list)

    task_start_list = {
    23: [1, 'Введите число n'],
    25: [1, 'Введите число a'],
    27: [1.1, 'Введите число, которое нужно проверить'],
    }

    input_value = []
    try:
        input_value = input_data(task_start_list[number_of_task])
    except KeyboardInterrupt:
        exit()
    call_program(number_of_task, input_value)


# 23 Задача Показать таблицу квадратов чисел от 1 до N

def degree_n(number):
    nw = []
    for i in range(1, number + 1):
        nw.append(i**2)
    return nw

# 25 Найти сумму чисел от 1 до А

def sum_cow(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum

# 27 Определить количество цифр в числе

def count_numeric_in_number(number):
    numb_str = str(number)
    count = 0
    for s in numb_str:
        if not (s == '-' or s == '.'):
            count += 1
    return count


change = [1, 'Введите номер задания: ']
interface(27)
