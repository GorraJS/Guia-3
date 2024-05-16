import requests, pyperclip
from bs4 import BeautifulSoup

def getArticle(url):
    pagina = requests.get(url)
    pagina.raise_for_status()
    if pagina.status_code == 200:
        soup = BeautifulSoup(pagina.text, 'html.parser')
        a = soup.find_all('article')
        return a

url = pyperclip.paste()

while True:
    if pyperclip.paste() != url:
        url = pyperclip.paste()
        web = requests.get(url)
        web.raise_for_status()
        if web.status_code == 200:
            soup = BeautifulSoup(web.text, 'html.parser')
            divs_with_links = soup.find_all('div', {'class': "sc-3c9f82-0 hLHwud"})
            print(pag)


