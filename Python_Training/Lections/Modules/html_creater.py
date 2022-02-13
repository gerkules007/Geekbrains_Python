from user_interface import *

def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device)) 
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += ' </body>\n</html>\n'

    with open('Python_Training/Lections/Modules/index.html', 'w') as page:
        page.write(html)
    return html

def create_collection(data, device = 1):
    t, p, w = data
    t = t + 32
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} F</p>\n'\
        .format(style, t)
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w) 
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += ' </body>\n</html>\n'

    with open('Python_Training/Lections/Modules/index.html', 'w') as page:
        page.write(html)
    return data