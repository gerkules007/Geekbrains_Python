from data_provider import data_collection

def create_collection():
    t, w, p = data_collection()
    xml = '<xml>\n'
    xml += '    <temperature units = "C">{}</temperature>\n'\
        .format(t)
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(w)
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml = '</xml>\n'

    with open('Python_Training/Lections/Modules/index1.xml', 'w') as page:
        page.write(xml)