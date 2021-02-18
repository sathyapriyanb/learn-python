import requests

from bs4 import BeautifulSoup
ind = int(input())
res = requests.get(input())
bs = BeautifulSoup(res.content, 'html.parser')
print((bs.find_all('h2')[ind]).text)
