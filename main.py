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


def convert(input_currency, input_amount, output_currency):
    if output_currency != "RON":
        output_amount = float(input_amount) * float(curs_valutar[input_currency]) / float(curs_valutar[output_currency])
    elif input_currency == output_currency:
        output_amount = input_amount
    else:
        output_amount = float(input_amount) * float(curs_valutar[input_currency])
    return output_amount


def get_available_currencies():
    currencies = []
    for key in curs_valutar:
        currencies.append(key)
    return currencies
