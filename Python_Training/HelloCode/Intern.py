# Задача 
# Вывести квадрат числа

numb = int(input('Введите число: '))

def Math_Pow(number):
    number = number**2
    return number

print(f'Квадрат числа: {Math_Pow(numb)}')