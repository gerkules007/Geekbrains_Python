#   Вводные функции

def input_data_interger(position):
    while True:
        try:
            data = int(input(f'Введите число {position}: '))
            break
        except Exception:
            continue
    return data

def input_list_interger(count):
    list = []
    for i in range(1, count + 1):
        list.append(input_data_interger(i))
    return list

print('Введите сколько чисел нужно для задачи')
count_numb = input_data_interger(1)
input_list = input_list_interger(count_numb)


# 15 Дано число. Проверить кратно ли оно 7 и 23

def true_ratio(list):
    n = list[0]
    k = list[1]
    return n % k

# 17 По двум заданным числам проверять является ли одно квадратом другого

def its_sqrt(list):
    n = list[0]
    s = list[1]
    return s == n*n

# 18 Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

def its_true(list):
    check = []
    for x in False, True:
        for y in False, True:
            check.append(not (x or y) == (not x and not y))
    return check
    

# 19 Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

def numb_of_quater(list):
    x = list[0]
    y = list[1]
    if x == 0 or y == 0:
        return 'Not Found'
    else:
        return {
        (x > 0 and y > 0): '1',
        (x < 0 and y > 0): '2',
        (x < 0 and y < 0): '3',
        (x > 0 and y < 0): '4'
    }[True]

# 20 Задать номер четверти, показать диапазоны для возможных координат

def quater_info(list):
    quat = {
        1: 'x > 0 and y > 0',
        2: 'x < 0 and y > 0',
        3: 'x < 0 and y < 0',
        4: 'x > 0 and y < 0)',
    }
    return quat[list[0]]

# 21 Программа проверяет пятизначное число на палиндромом.

def palindrom(list):
    n = str(list)
    i = 0
    result = True
    if n.find('-') or n.find('.'):
        n = n[1:]
        n.replace('.', '')
    print(n)
    while (i < len(n) // 2):
        if n[i] != n[-(i+1)]:
            result = False
            break
        i += 1
    return result

# 22 Найти расстояние между точками в пространстве 2D/3D



print(its_true(input_list))