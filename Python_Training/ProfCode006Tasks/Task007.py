# Даны четыре логические значения f1, f2, f3, f4. Записать условие того, что
# - более трёх значений истинны
# - хотя бы три значения истинны
# - менее трёх значений истинны

f1 = not (0 and 1)
f2 = not (0 and 1)
f3 = not (0 and 1)
f4 = not (0 and 1)

list_i = [f1, f2, f3, f4]

def its_true(list):
    true_false_list = []
    for i in range(0, len(list)):
        j = i + 1
        while j < len(list):
            print(f'({i}, {j})')
            if list[i] == list[j]:
                true_false_list.append(True)
            else:
                true_false_list.append(False)
            j += 1
    return true_false_list

def check_its_true(list):
    arr_list = its_true(list)
    count = 0
    check_list = [False, False, False]
    for i in arr_list:
        if i == True: count += 1
    if count > 3: check_list[0] = True
    if count == 3: check_list[1] = True
    if count < 3: check_list[2] = True
    return check_list

print_arr = check_its_true(list_i)
print(f'более трёх значений истинны: {print_arr[0]}\nхотя бы три значения истинны: {print_arr[1]}\nменее трёх значений истинны: {print_arr[2]}')

