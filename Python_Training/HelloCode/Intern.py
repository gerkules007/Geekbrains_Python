

number1 = int(input('Введите число 1: '))
# number2 = int(input('Введите число 2: '))
# number3 = int(input('Введите число 2: '))
# list_number = [number1, number2, number3]

# Задача 0 Вывести квадрат числа

def Math_Pow(number):
    number = number**2
    return number

# Задача 2 Даны два числа. Показать большее и меньшее число

def compare(list):
    if list[0] > list[1]:
        print(f'Число {list[0]} = большее, а {list[1]} = меньшее')
    elif list[0] < list[1]:
        print(f'Число {list[1]} = больше, а {list[0]} = меньшее')
    else:
        print('Числа равны')

# Задача 4 Найти максимальное из трех чисел

def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

# Задача 6 Выяснить является ли число чётным

def even_number(numb1):
    return (numb1 % 2 == 0)

# Задача 8 Показать четные числа от 1 до N

def show_even_number(n):
    result = []
    for i in range(1,n+1):
        if i % 2 == 0:
            result.append(i)
    return result

# Задача 10 Показать вторую цифру трёхзначного числа

def second_number(n):
    result = (n % 100) // 10
    return result

# Задача 12 Удалить вторую цифру трёхзначного числа

def delete_second_number(n):
    one = (n // 100) * 10
    third = n % 10
    return one + third

# Задача 14 Найти третью цифру числа или сообщить, что её нет

def find_third_numb(n):
    if n // 100 != 0:
        print(n % 1000 // 100)
    else:
        print('Not exist')


find_third_numb(number1)
print()