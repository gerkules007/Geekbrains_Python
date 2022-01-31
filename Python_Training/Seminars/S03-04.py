import random
from cmath import sqrt
import math
import time
# 11 Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
def crt_arr_base_on_three(n):
    return [(-3)**i for i in range(n+1)]

# 12 Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.
def crt_dic_with_N(n):
    return {i: 3*i + 1 for i in range(1, n)}

# 13 Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
def count_string_values(n):
    s, f = n[0], n[1]
    return s.count(f)

# 14  Подсчитать сумму цифр в вещественном числе.
def sum_of_real_numb(n):
    numb_str = str(n)
    sum = 0
    for s in numb_str:
        if not (s == '-' or s == '.'):
            sum += int(s)
    return sum

# 15 Написать программу получающую набор произведений чисел от 1 до N. 
#    Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
def set_of_multiple(n):
    return 1 if n == 1 else set_of_multiple(n-1)*n

def fill_miltiple(n):
    return [set_of_multiple(i) for i in range(1,n+1)]

# 16 Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
def crt_dic_with_N2(n):
    return sum([((1 + (1 / i))**i) for i in range(1, n + 1)])

# 17 Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число


# 18 Реализовать алгоритм перемешивания списка. 
def shake_list1(n):
    for i in range(len(n)):
        x = random.randint(0, len(n)-1)
        y = random.randint(0, len(n)-1)
        n.insert(x, n.pop(y))
    return n

def shake_list2(n):
    random.shuffle(n)

# 19 Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
def randomize_it(n):
#     start = n[0]
#     end = n[1]
#     sec = time.time()
#     x = sec%1
    return

# 20 Определить, присутствует ли в заданном списке строк, некоторое число
# (использовать переменную 'а')
def find_number(n): return n[1] in n[0]

# 21 Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
# def find_string_element(n):
#     return (n[n.index('\n') + 1:])

# 22 Найти сумму чисел списка стоящих на нечетной позиции
def sum_not_even_numbers(n): 
    return sum(n[1::2])

# 23 Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
def palidrom_multiply(n):
    return [n[i]*n[-i-1] for i in range((len(n)+1)//2)]


# 24 В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def find_min_real_after_dot(n):
    a = [ i%1 for i in n if i%1 != 0 ]
    return round(max(a) - min(a), 15)

# 25 Написать программу преобразования десятичного числа в двоичное
def binary_parse(n, bit_len = 8, b = ''):
    while n > 0: 
        b = str(n%2) + b
        n = n // 2
    if len(b) < bit_len: b = '0'*(bit_len-len(b)) + b
    return b

def binary_parse2(n): return bin(n)[2:]

# 26 Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
def fibonacci(n):
    return fibonacci(n-2) + fibonacci(n-1) if n > 2 else 1

def fill_fibonacci(n):
    return {i: fibonacci(i) for i in range(1, abs(n)+1)} if n > 0 else {-i: -fibonacci(i) for i in range(1, abs(n)+1)}

# 27 Строка содержит набор чисел. Показать большее и меньшее число
def min_max_string(n, splitter = ','):
    return (min(int(i) for i in n.split(splitter)), max(int(i) for i in n.split(splitter)))

# 28 Найти корни квадратного уравнения Ax² + Bx + C = 0, пользуясь а) Математикой б) Используя дополнительные библиотеки*
# в square_equation(n) для x^2 - 2x + 3 
# выдает ((1+1.4142135623730951j), (0.9999999999999999-1.4142135623730951j)), округлить не получается
def square_equation(n):
    a, b, c = n[0], n[1], n[2]
    D = round(b**2 - (4 * a * c), 5)
    # опустил проверку D>0, D<0, D == 0, чтобы считать и мнимые числа
    x1 = +(D**0.5 / (2 * a)) - round((b / (2 * a)), 5)
    x2 = -(D**0.5 / (2 * a)) - round((b / (2 * a)), 5)
    return (x1, x2)

# enter cmath (вывод комплексных чисел)
def square_equation_library(n):
    a, b, c = n[0], n[1], n[2]
    D = round(b**2 - (4*a*c), 5)
    x1 = +(sqrt(D) / (2*a)) - round((b / (2*a)), 5)
    x2 = -(sqrt(D) / (2*a)) - round((b / (2*a)), 5)
    return (x1, x2)

# 30 Вычислить число pi c заданной точностью d
# был вариант math.pi // n * n, но не давал точного знака при умножении n
def pi_number(n):
    x = abs(int(math.log10(n)))
    return round(math.pi, x)


def call_program(task, value_list):
    call = {
        11: crt_arr_base_on_three,
        12: crt_dic_with_N,
        13: count_string_values,
        14: sum_of_real_numb,
        15: fill_miltiple,
        16: crt_dic_with_N2,
        18: shake_list1,
        18.1: shake_list2,
        19: randomize_it,
        20: find_number,
        22: sum_not_even_numbers,
        23: palidrom_multiply,
        24: find_min_real_after_dot,
        25: binary_parse,
        25.1: binary_parse2,
        26: fill_fibonacci,
        27: min_max_string,
        28: square_equation,
        28.1: square_equation_library,
        30: pi_number
    }
    print(call[task](value_list))

a = [[4,5,7], 4]
b = [1,2,3,4,5,6,7]
c = [1.1, 1.01, 1.001]
v13 = ["25,17,31,25", '31']
v24 = [1.1, 1.2, 3.1, 5, 10.01]
call_program(24, v24)