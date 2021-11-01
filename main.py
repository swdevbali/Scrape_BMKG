"""
This project will get the latest information about earthquake from bmkg.go.id
"""
from bs4 import BeautifulSoup

author = 'Eko SW'
date = '1 November 2022'
url = 'https://www.bmkg.go.id/'

import requests
result = requests.get(url)
result = BeautifulSoup(result.text, 'html.parser')
print(result.title.string)