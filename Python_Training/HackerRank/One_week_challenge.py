def input_x(): return [1,5]
print(*input_x())

# Преобразовать аналоговое время в полное
s = '11:00:00PM'
def time_o_clock(s):
    time_code = s[-2:].upper()
    start_time = int(s[:2])
    hour_now = 0 if start_time == 12 else start_time
    hour_now = hour_now + 12 if time_code == 'PM' else hour_now
    new_s = str(hour_now) + s[2:-2] if hour_now >= 10 else '0' + str(hour_now) + s[2:-2]
    print(new_s)

# Печать с условиями (требует изучения нового материала)
def fizz_buzz(i):
    for n in range(1, i+1):
        one = ''
        two = ''
        three = ''
        if not n % 3: one = 'Fizz'
        if not n % 5: two = 'Buzz'
        if n % 3 and n % 5:
            three = str(n)
        print((one + two + three))

# Найти модуль разности левой и правой диагонали двухмерного массива 
def diagonalDifference(arr):
    x = sum([arr[i][i] for i in range(len(arr))])
    y = sum([arr[-i-1][i] for i in range(len(arr))])
    return abs(x-y)

lst1 = [
    [11,2,4,4],
    [4,5,6,5],
    [10,8,-12,-7],
    [4,5,6,5],
]
# print(diagonalDifference(lst1))

# Посчитать в массиве количество элементов для метода сортировки посчетом (в условии указаны только положительные элементы)
def countingSort(arr):
    calc_arr = [0]*(max(arr)+1)
    for i in arr: calc_arr[i] += 1
    return calc_arr
lst2 = [1,3,4,32,5,11,2,5,32,23,7,4]
# print(countingSort(lst2))


# Необходимо отсортировать двухмерный массив так, чтобы максимальные числа были в первом квотаре этого массива
# Сортировать можно только путем переворачивания колонок и строк
matx = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

def flippingMatrix(matrix):
    quater = len(matrix) // 2
    for y in range(len(matrix)):
        cur_arr = [matrix[y][x] for x in range(len(matrix))]
        val = max(cur_arr)
        q_arr = []
        for j in range(quater):
            for k in range(quater):
                q_arr.append(matrix[j][k])
        if not val in q_arr: 
            cur_arr.reverse()
            for i in range(len(matrix)): matrix[y][i] = cur_arr[i]
        for i in range(len(matrix)): print(matrix[i])
        print()
    for x in range(len(matrix)):
        cur_arr = [matrix[y][x] for y in range(len(matrix))]
        val = max(cur_arr)
        q_arr = []
        for j in range(quater):
            for k in range(quater):
                q_arr.append(matrix[j][k])
        if not val in q_arr: 
            cur_arr.reverse()
            for i in range(len(matrix)): matrix[i][x] = cur_arr[i]
        for i in range(len(matrix)): print(matrix[i])
        print()

# flippingMatrix(matx)

