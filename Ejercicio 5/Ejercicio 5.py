import requests,os,pyperclip
from bs4 import BeautifulSoup


while True:
    url = 'https://listado.mercadolibre.com.ar/'
    print('Ingrese producto:')
    producto = input()
    url += producto

    selectProduct = [] 
    nameFile = 'PRODUCTOS.txt'


    web = requests.get(url)
    web.raise_for_status()

    if web.status_code == 200:
        html = BeautifulSoup(web.text, 'html.parser')
        li = html.find_all('div', {'class' : 'ui-search-result__content-wrapper'})

        playFile = open(nameFile,'w')


        for i in li[:5]:

            #Nombre
            nameProduct = i.find('h2').text
            playFile.write(f'Producto: {nameProduct}\n')

            #Tienda
            tienda = i.find('p').text
            playFile.write(f'Tienda: {tienda}\n')

            #Precio
            price = i.find('span', {'class' : 'andes-money-amount__fraction'}).text
            playFile.write(f'Precio: {price}\n')

            #GTA 
            stars = i.find('span', {'class' : 'ui-search-reviews__rating-number'})
            if stars:
                stars = stars.text
                playFile.write(f'Clasificacion: {stars}\n')
            else:
                playFile.write('Clasificacion: NO HAY CLASIFICACION\n')

            #salto de linea
            playFile.write('\n')

        playFile.close()
        
        