import pyperclip,requests
from bs4 import BeautifulSoup  

url = None
lista = []

while True:
    aurl = pyperclip.paste()
    if aurl != url:
        burl = requests.get(aurl)
        if burl.status_code == 200:
            burl.raise_for_status()        
            soup = BeautifulSoup(burl.text, 'html.parser')
            p = soup.find_all('p')

            lista.append(p)

            url = burl
            print(p)