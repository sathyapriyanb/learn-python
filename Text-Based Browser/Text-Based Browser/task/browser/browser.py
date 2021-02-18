import argparse
import collections
import os

import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

init(autoreset=True)
parser = argparse.ArgumentParser(description='Get the directory to store filles')
parser.add_argument('dir')
args = parser.parse_args()
folder = os.path.join(os.getcwd(), args.dir)
print(os.getcwd(), args.dir, folder)
if not os.access(folder, os.W_OK):
    os.mkdir(folder)
history = collections.deque()

while True:
    website = input()
    if website == 'back':
        history.pop()
        website = history.pop()
    else:
        history.append(website)
    file_name = os.path.join(folder, website.split(".")[0])
    if website == 'exit':
        break
    elif not website.find('.') >= 0:
        if os.access(file_name, os.F_OK):
            with open(file_name, 'r') as f:
                print(f.read())
        else:
            print("error")
    else:
        text = None
        res = None

        if os.access(file_name, os.F_OK):
            with open(file_name, 'r') as f:
                print(f.read())
        else:
            if website.find('http://') < 0 and website.find('https://') < 0:
                website = 'http://' + website
            try:
                res = requests.get(website)
            except Exception:
                print("Incorrect URL")
            else:
                soup = BeautifulSoup(res.content, 'html.parser')
                #(<p>, headers, <a> and <ul>, <ol>, <li>)
                elements = soup.find_all(('p', 'h1', 'h2', 'h3', 'h4', 'a', 'ul', 'ol', 'li'))
                # text = soup.get_text()
                with open(file_name, 'w') as f:
                    for element in elements:
                        if element.name == 'a':
                            element_text = Fore.BLUE + element.text
                        else:
                            element_text = element.text
                        print(element_text)
                        f.write(element_text)
