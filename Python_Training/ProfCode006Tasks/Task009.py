# Проверить, что точка с координатами (x, y) принадлежит фигуре
#   1          2          3 
# █████      █████      █   █
# █   █      █   █      █   █
# █   █      █████      █   █
# █   █          █      █████

first_figure = [
    '█████',
    '█   █',
    '█   █',
    '█   █',
]

second_figure = [
    '█████',
    '█   █',
    '█████',
    '    █',
]

third_figure = [
    '█   █',
    '█   █',
    '█   █',
    '█████',
]

point = (3,3)

figures = [first_figure, second_figure, third_figure]

def check_figures(i_figure, points):
    check = []
    for i in i_figure:
        print_figure(i)
        check.append(find_point_in_figure(i, points))
        print(check[len(check) - 1])
    return check

def find_point_in_figure(figure, p):
    return True if figure[p[0]][p[1]] != ' ' else False

def print_figure(figure):
    for i in figure:
        print(i)

print(check_figures(figures, point))