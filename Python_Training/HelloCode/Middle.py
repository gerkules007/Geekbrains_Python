# Вводные функции

def input_data(set_up_list):
    for i in range(1, len(set_up_list)):
        while True:
            new_data = check_input_data(input(f'{set_up_list[i]}: '))
            if type(new_data) == type(set_up_list[0]):
                break
    return new_data

def check_input_data(data):
    try:
        input_type = int(data)
    except ValueError:
        try:
            input_type = float(data)
        except ValueError:
            try:
                input_type = str(data)
            except ValueError:
                print('Unindentify type')
    return input_type

# def input_list_interger(count):
#     list = []
#     for i in range(1, count + 1):
#         list.append(input_data_interger(i))
#     return list

# input_list = input_list_interger(3)
def interface(number_of_task):
    formats_of_data = {
        'int' : 1,
        'float' : 1.1,
        'str': 'str'
    }

    task_list = {
        23: [formats_of_data['int'], 'Введите число n']
        }

    input_value = []
    try:
        input_value = input_data(task_list[number_of_task])
    except KeyboardInterrupt:
        exit()
    

interface(23)
