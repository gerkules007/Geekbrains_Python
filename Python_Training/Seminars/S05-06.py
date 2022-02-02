import time

#32 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
def unique_elements(lst):
    return

def call_program(task, value_list):
    start_t = time.time()
    call = {
        32: unique_elements,
    }
    print(call[task](value_list))
    print(f'Result timer: {round(time.time() - start_t, 4)} sec')

v32 = [4,5,7]

call_program(32,v32)