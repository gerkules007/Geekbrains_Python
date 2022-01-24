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
    call = {
        23: degree_n,
        24: cub_number,
        25: sum_cow,
        27: count_numeric_in_number,
        29: multiply_cow
    }
    print(call[task](value_list))

def interface(number_of_task):

    task_start_list = {
    23: [1, 'Введите число n'],
    24: [1, 'Введите число n'],
    25: [1, 'Введите число a'],
    27: [1.1, 'Введите число, которое нужно проверить'],
    29: [1, 'Введите число n'],
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

# 24 Найти кубы чисел от 1 до N

def cub_number(number):
    return [n**3 for n in range(1, number + 1)]

# 25 Найти сумму чисел от 1 до А

def sum_cow(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum

# 26 Возведите число А в натуральную степень B используя цикл

def get_number(number):
    temp = 1
    a = number[0]
    for n in range(number[1]):
        temp *= a
    return temp

# 27 Определить количество цифр в числе

def count_numeric_in_number(number):
    numb_str = str(number)
    count = 0
    for s in numb_str:
        if not (s == '-' or s == '.'):
            count += 1
    return count

# 28 Подсчитать сумму цифр в числе

def sum_in_numb(number):
    new_numb = 0
    for i in number:
        if not (i == '-' or i == '.'):
            new_numb += int(i)
    return new_numb

# 29 Написать программу вычисления произведения чисел от 1 до N

def multiply_cow(number):
    multi = 1
    for i in range(1, number + 1):
        multi *= i
    return multi

# 30 Показать кубы чисел, заканчивающихся на четную цифру

def cub_even_numbers(number):
    return [n**3 for n in number if n%2 == 0]

change = [1, 'Введите номер задания: ']
interface(24)

