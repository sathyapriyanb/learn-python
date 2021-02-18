import re

import requests

from bs4 import BeautifulSoup

word = input()
res = requests.get(input())
bs = BeautifulSoup(res.content, 'html.parser')
p = bs.find('p', text=re.compile(f'.*{word}.*'))
print(p.text)
