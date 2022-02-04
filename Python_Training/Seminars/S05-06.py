from ast import keyword
import time
import random
from functools import *

#32 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
def unique_elements(l):
    return list(set(l))

# 33 Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
def create_square_equation(k, min = 0, max = 1, s = '', l : list = []):
    d = [random.randint(min, max) for _ in range(k)]
    if k >= 2: 
        for i in range(2, len(d)):
            if d[i] != 0:
                l.append(str(d[i]) + '*x^' + str(i))
    if d[1] != 0: l.append(str(d[1]) + '*x')
    if d[0] != 0: l.append(str(d[0]))
    for i in l[:-1]: 
        s += i + ' + '
    z = type(reduce(lambda x,y: x + y, l[:-1]))
    s += l[-1] + ' = 0'
    open("Python_Training\\Seminars\\xfile.txt", 'w').write(s)

    # if k >= 2:
    #     for i in range(2, k):
    #         l.append(str(random.randint(min, max)) + '*x^' + str(i))
    # if d[1] != 0: l.append(str(d[1]) + '*x')
    # if d[0] != 0: l.append(str(d[0]))
    # for i in l[:-1]: s += i + ' + '
    # s += l[-1] + ' = 0'

    # max = random.randint(min, max+1)
    # if k == 0 or max == 0: return '0'
    # s = ''
    # while k > 0 or max < 0:
    #     r = random.randint(min, max)
    #     if r != 0:
    #         max -= r
    #         if k > 1: s = str(r) + '*x^' + str(k) + ' + '
    #         else: s += str(r) + '*x + '
    #     k -= 1
    # if max != 0: s += str(max) + ' = 0'
    # else: s = s[:-2] + '= 0'
    return 'Done'

# 34 Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

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
# def many_lists(l, nl = []):
#     for i in range(len(l)):
#         temp = []
#         for j in range(i+1, len(l)-1):
#             temp.append(l[j])
#             for k in range(i+1, j):
#                 if l[k] < l[k+1]: temp.append(l[k])
#             nl.append(temp)
#     return nl

# 37 Дан список чисел. Выделить среди них максимальное количество чисел, 
# удовлетворяющих условию предыдущей задачи. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]

# 38 Напишите программу, удаляющую из текста все слова содержащие "абв".
def del_text(l: str):
    with open("Python_Training\\Seminars\\xfile.txt", 'r') as f:
        x = f.read().replace(l, '')
    with open("Python_Training\\Seminars\\xfile.txt", 'w') as f:
        f.write(x)
    return 'Delete done'

# 42 Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных файлах

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
        35: find_number_for_r,
        36: many_lists,
        38: del_text,
        43: lonely_elements
    }
    print(call[task](value_list))
    print(f'Result timer: {round(time.time() - start_t, 4)} sec')

v32 = [4,5,7,4,4,5,5,7]
v36 = [1, 5, 2, 3, 4, 6, 1, 7]
test = [1,2,3,4]
txt = 'ab'
v43 = [1, 2, 3, 5, 1, 5, 3, 10]

call_program(43, v43)