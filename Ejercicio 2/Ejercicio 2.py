import pyperclip,requests
from bs4 import BeautifulSoup  

url = None

while True:
    aurl = pyperclip.paste()
    if aurl != url:
        burl = requests.get(aurl)
        if burl.status_code == 200:
            burl.raise_for_status()        
            soup = BeautifulSoup(burl.text, 'html.parser')
            p = soup.find_all('p')
            
            for i in range(len(p)):
                p[i] = p[i].string
                
            url = burl
            print(p)