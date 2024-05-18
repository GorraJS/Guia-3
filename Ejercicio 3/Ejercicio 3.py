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
            soup = BeautifulSoup(web.txt, 'html.parser')
            divsLinks = soup.find_all('div', {'class': "sc-3c9f82-0 hLHwud"})
            for div in divsLinks:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    print(href)
                    