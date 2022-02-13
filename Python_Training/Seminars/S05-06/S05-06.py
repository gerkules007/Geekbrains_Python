import time
import random
from functools import *

#32 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
def unique_elements(l):
    return list(set(l))

# 33 Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
def create_square_equation(k, min = 0, max = 1, s = None):
    d = {i: random.randint(min, max) for i in range(k, -1, -1)}
    d[0] = None if d[0] == 0 else str(d[0])
    for i in range(1, len(d)):
        if d[i] > 1: 
            d[i] = str(d[i]) + '*x'
        elif d[i] == 1:
            d[i] = 'x'
        else: d[i] = None
    for i in range(2, len(d)):
        if d[i] != None:
            d[i] = d[i] + '^' + str(i)
    # print(d)
    s = " + ".join([d[i] for i in d.keys() if d[i] != None]) + ' = 0'
    # print(s)
    try:
        open("Python_Training\\Seminars\\xfile.txt", 'w').write(s)
        return 'Done'
    except Exception:
        return 'Don\'t write file'

# 34* Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
def merge_square_equation(l, s = ''):
    path1, path2 = l[0], l[1]
    f1 = open(path1, 'r').read().split(' ')
    f2 = open(path2, 'r').read().split(' ')
    delete_chars = ['=', '0', '+']
    f = list(filter(lambda x: not x in delete_chars, f1)) + \
        list(filter(lambda x: not x in delete_chars, f2))
    s = calculate_square_equation(f)
    # s = " + ".join([i for i in fs]) + ' = 0'
    # try:
    #     open("Python_Training\\Seminars\\xfile.txt", 'w').write(s)
    #     return 'Done'
    # except Exception:
    #     return 'Don\'t write file'
    return s

def calculate_square_equation(m):
    d1 = {x[x.index('^')+1]: x[:x.index('x')] for x in m if '^' in x}
    return d1

# 35 В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
# Было добавлена перезапись файла с восстановлением последовательности
def find_number_for_r(l):
    l = list(map(int, open("Python_Training\\Seminars\\xfile.txt", 'r').read().split(' ')))
    for i in range(1,len(l)):
        if l[i] - 1 != l[i-1]:
            l.insert(i, l[i] - 1)
            m = ' '.join([str(i) for i in l])
            open("Python_Training\\Seminars\\xfile.txt", 'w').write(m)
            return 'Done'
    return 'Not found'
    # return str([l[i]-1 if l[i] - 1 != l[i-1] else 'Not found' for i in range(1,len(l))])

# 36 Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя
def many_lists(l, nl = []):
    for j in range(len(l)-1):
        temp = []
        temp.append(l[j])
        for i in range(j+1, len(l)):
            if l[j] < l[i]:
                if temp[len(temp)-1] < l[i]:
                    temp.append(l[i])
                    new_temp = tuple(temp)
                    nl.append(list(new_temp))
                else:
                    temp.pop()
                    temp.append(l[i])
                    new_temp = tuple(temp)
                    nl.append(list(new_temp))
    return nl

# 37* Дан список чисел. Выделить среди них максимальное количество чисел, 
# удовлетворяющих условию предыдущей задачи. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# Порядок элементов менять нельзя
def max_many_lists(l):
    nl = many_lists(l)
    k = max([(len(n), i) for i, n in enumerate(nl)])
    return nl[k[1]]

# 38 Напишите программу, удаляющую из текста все слова содержащие "абв".
def del_text(l: str):
    with open("Python_Training\\Seminars\\xfile.txt", 'r') as f:
        x = f.read().replace(l, '')
    with open("Python_Training\\Seminars\\xfile.txt", 'w') as f:
        f.write(x)
    return 'Delete done'

# 39 Создать игру с конфетами
# НАХОДИТСЯ В ФАЙЛЕ 39_candy_game

# 40* Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
# НАХОДИТСЯ В ФАЙЛЕ 40_cross_zero

# 41* Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. 
# приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
# Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;
def calc_string_expression(s: str):
    try:
        return eval(s)
    except Exception:
        print('Error reading string expression')
        return 0

# 42 Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных файлах
def rle_get(d, byte = 256):
    count, s = 1, ''
    try:
        f = open(d[0], 'r').read()
        new_char = f[0]
        for i in range(1,len(f)):
            if new_char != f[i]:
                s += str(count) + new_char
                count = 1
                new_char = f[i]
            else:
                count += 1
                if byte < count:
                    s += str(count) + new_char
                    count = 1
                    continue
        s += str(count) + new_char  
        if len(f) <= len(s): s = f
        with open(d[1], 'w') as f2:
            f2.write(s)
    except Exception:
        return 'Error compilation'
    else:
        return 'Done'


# 43 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
def lonely_elements(l):
    nw = {i: 0 for i in l}
    for i in range(len(l)):
        if l[i] in nw: 
            nw[l[i]] += 1
    return [i for i in list(nw.keys()) if nw[i] == 1]

def call_program(task, value_list):
    start_t = time.time()
    call = {
        32: unique_elements,
        33: create_square_equation,
        34: calculate_square_equation,
        34.1: merge_square_equation,
        35: find_number_for_r,
        36: many_lists,
        37: max_many_lists,
        38: del_text,
        41: calc_string_expression,
        42: rle_get,
        43: lonely_elements,
    }
    print(call[task](value_list))
    print(f'Result timer: {round(time.time() - start_t, 4)} sec')

v32 = [4,5,7,4,4,5,5,7]
v36 = [1, 5, 2, 3, 4, 6, 1, 7]
test = [1,2,3,4]
txt = 'ab'
v43 = [1, 2, 3, 5, 1, 5, 3, 10]
v34_41 = ["Python_Training\\Seminars\\xfile.txt", "Python_Training\\Seminars\\xfile2.txt"]
v41 = '((4-2)*(1+3))/10'
call_program(42, v34_41)