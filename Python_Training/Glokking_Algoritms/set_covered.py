set_states = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
result = set()
stations = {1: set(['a', 'b', 'c']), 2: set(['f', 'e', 'd']), 3: set(['b', 'e', 'g']), 4: set(['d', 'f']), 5: set(['g', 'h'])}

while set_states: #                             пока все станции не покроются
    best_station = None #                           сбрасываем станцию для сравнения
    station_container = set() #                     контейнер для радиовышек лучшего покрытия
    for s_key, s_value in stations.items(): #           проверяем все станции в области
        is_covered_place = set_states & s_value #               |
        if len(is_covered_place) > len(station_container): #    | 
            best_station = s_key #                              | из всех станций находим лучшую по покрытию оставшиейся области
            station_container = is_covered_place #              |
    set_states = set_states - station_container #   лучшую отнимаем от всей зоны покрытия
    result.add(best_station) #                  добавляем в список лучшую станцию
    stations.pop(best_station) #                удаляем найденную станцию из поиска

print(result)