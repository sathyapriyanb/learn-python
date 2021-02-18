import requests

from bs4 import BeautifulSoup

response = requests.get(input())
bs_text = BeautifulSoup(response.content, 'html.parser')
print(bs_text.find('h1').text)
