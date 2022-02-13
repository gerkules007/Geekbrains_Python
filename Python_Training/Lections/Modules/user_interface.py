import data_provider as pr
import logger as log

def temperature_view(sensor):
    data = pr.get_temperature(sensor)
    log.temperature_logger(data)
    return data

def pressure_view(sensor):
    data = pr.get_pressure(sensor)
    log.pressure_logger(data)
    return data

def wind_speed_view(sensor):
    data = pr.get_wind_speed(sensor)
    log.wind_speed_logger(data)
    return data