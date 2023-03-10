import requests
from bs4 import BeautifulSoup


url = 'https://crfam.org.br/'

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')


lista_div = soup.find_all('div',class_='center')

for lista in lista_div:
    valores = lista.find_all('h2', class_='titulo-secao f-left')
    for resultado in valores:
        print(resultado.next_element)