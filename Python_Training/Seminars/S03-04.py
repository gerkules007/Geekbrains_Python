import random
from cmath import sqrt
import math
# 11 Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
def crt_arr_base_on_three(n):
    return [(-3)**i for i in range(n+1)]

# 12 Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.
def crt_dic_with_N(n):
    return {i: 3*i + 1 for i in range(1, n)}

# 14  Подсчитать сумму цифр в вещественном числе.
def sum_of_real_numb(n):
    numb_str = str(n)
    sum = 0
    for s in numb_str:
        if not (s == '-' or s == '.'):
            sum += int(s)
    return sum

# 16 Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
def crt_dic_with_N2(n):
    return sum([((1 + (1 / i))**i) for i in range(1, n + 1)])

# 18 Реализовать алгоритм перемешивания списка. 
def shake_list1(n):
    for i in range(len(n)):
        x = random.randint(0, len(n)-1)
        y = random.randint(0, len(n)-1)
        n.insert(x, n.pop(y))
    return n

def shake_list2(n):
    random.shuffle(n)
    return n

# 20 Определить, присутствует ли в заданном списке строк, некоторое число
def find_number(n): return n[1] in n[0]

# 22 Найти сумму чисел списка стоящих на нечетной позиции
def sum_not_even_numbers(n): 
    return sum([i for i in n if i % 2 != 0])

# 24 В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def find_min_real_after_dot(n):
    a = [ round( i%1 , 7) for i in n]
    return max(a) - min(a)

# 26 Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
def fibonacci(n):
    return fibonacci(n-2) + fibonacci(n-1) if n > 2 else 1

def fill_fibonacci(n):
    return {i: fibonacci(i) for i in range(1, abs(n)+1)} if n > 0 else {-i: -fibonacci(i) for i in range(1, abs(n)+1)}

# 28 Найти корни квадратного уравнения Ax² + Bx + C = 0, пользуясь а) Математикой б) Используя дополнительные библиотеки*

# в square_equation(n) для x^2 - 2x + 3 
# выдает ((1+1.4142135623730951j), (0.9999999999999999-1.4142135623730951j)), округлить не получается

# опустил проверку D>0, D<0, D == 0
def square_equation(n):
    a = n[0]
    b = n[1]
    c = n[2]
    D = round(b**2 - (4 * a * c), 5)
    x1 = +(D**0.5 / (2 * a)) - round((b / (2 * a)), 5)
    x2 = -(D**0.5 / (2 * a)) - round((b / (2 * a)), 5)
    return (x1, x2)

# enter cmath (вывод комплексных чисел)
def square_equation_library(n):
    a = n[0]
    b = n[1]
    c = n[2]
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
        14: sum_of_real_numb,
        16: crt_dic_with_N2,
        18: shake_list1,
        18.1: shake_list2,
        20: find_number,
        22: sum_not_even_numbers,
        24: find_min_real_after_dot,
        26: fill_fibonacci,
        28: square_equation,
        28.1: square_equation_library,
        30: pi_number
    }
    print(call[task](value_list))

a = [[4,5,7], 4]
b = [1,2,3,4,5,6,7]
c = [1.1, 1.01, 1.001]
call_program(30, 0.00000001)