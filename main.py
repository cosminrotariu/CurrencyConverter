from bs4 import BeautifulSoup
import requests

url = 'https://www.bnr.ro/Cursul-de-schimb-524.aspx'
req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")

rows = soup.findAll('tr')
curs_valutar = dict()

for i in range(1, len(rows)):
    cols = [t.text.rstrip().replace(',', '.') for t in rows[i].find_all('td')]
    curs_valutar.update({cols[1]: cols[6]})

for key in curs_valutar:
    print("1 " + key + " -> " + curs_valutar[key] + " RON")

suma_intrare = input("Suma pe care o vreti sa o convertiti: ")
moneda_intrare = input("Moneda intrare: ")
moneda_iesire = input("Moneda iesire: ")

if moneda_iesire != "RON":
    suma_iesire = float(suma_intrare) * float(curs_valutar[moneda_intrare]) / float(curs_valutar[moneda_iesire])
else:
    suma_iesire = float(suma_intrare) * float(curs_valutar[moneda_intrare])

print(suma_iesire, " ", moneda_iesire)
