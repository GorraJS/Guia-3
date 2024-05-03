import pyperclip,requests

url = ''
while True:
    burl = pyperclip.paste()
    if burl != url:
        url1 = requests.get(burl)
        url1.raise_for_status()
        html = open('./Ejercicio 1/Web.html', 'wb')
        for chunk in url1.iter_content(100000):
            html.write(chunk)
        url = burl
        print(burl)