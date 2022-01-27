from bs4 import BeautifulSoup as bs
import re
import requests


def tableFactorize(trackingCode, searchTag):
    link = "https://www.aex.com.py/web/tracking.php?guia="

    # Se descompone la pagina para buscar la tabla
    data = requests.get(link+trackingCode)
    pageContent = bs(data.content, 'html.parser')
    tableTag = pageContent.find_all(searchTag)[0:4]


    # expresion regular para traer el contenido dentro de los tags
    patron = re.compile('>(.+?)<')
    content = []

    # se recorre las filas para aplicar la expresion regular
    for row in tableTag:
        row = patron.findall(str(row))
        # Si existe contenido, se agrega el primer elemento con el [0]
        if row:
            content.append(row[0])

    return content


def responseFilter(idTracking):
    tableContent = tableFactorize(idTracking, 'td')

    # Se define las cabeceras de la tabla
    tableHeaders = tableFactorize(idTracking, 'th')
    # Se inicializa la variable de la respuesta a enviar porque todavia no sabemos enviar un diccionario para telegram
    sendResponse = ""

    # Se formatea el msj dependiendo del tamaño de la tabla con sus respectivas cabeceras
    for i in range(len(tableContent)):
        sendResponse = sendResponse + f'{tableHeaders[i]}: {tableContent[i]} \n\n'

    return sendResponse

