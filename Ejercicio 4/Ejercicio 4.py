import pyperclip,requests,os
from bs4 import BeautifulSoup

url = pyperclip.paste() #Url usada: https://www.nasa.gov/ames/papers-for-download/
nameFile = 'PFDs'
pdf = []

while True:
    if pyperclip.paste() != url:
        url = pyperclip.paste()
        web = requests.get(url)
        web.raise_for_status()
        if web.status_code == 200:
            html = BeautifulSoup(web.text, 'html.parser')
            p = html.find_all('p')

            for i in p:
                a = i.find_all()
                for j in a:
                    href = j.get('href')
                    if href and '.pdf' in href:
                        pdf.append(href)

        if pdf:
            os.makedirs(nameFile, exist_ok=True)
            for urlPdf in pdf:
                arch = requests.get(urlPdf)
                arch.raise_for_status()
                if arch.status_code == 200:
                    playFile = open(os.path.join(nameFile, os.path.basename(urlPdf)),'wb')
                    for chunk in arch.iter_content(10000):
                        playFile.write(chunk)
