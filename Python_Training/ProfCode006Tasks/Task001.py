# Подсчитать количество натуральных чисел, не превосходящих заданного числа n, которые

# делятся на k, но не на l
# делятся хотябы на k или на l
# не делятся на (k + l)

min = 0
max = 50
k = 4
l = 3

def conduction_ratio(min, max):
    count = [0,0,0]
    for i in range(min,max):
        if i % k == 0 and i % l != 0:
            count[0] += 1
        if i % k == 0 or i % l == 0:
            count[1] += 1
        if i % (k + l) == 0:
            count[2] += 1
    return count

print(conduction_ratio(min, max))