"""
This project will get the latest information about earthquake from bmkg.go.id
"""
import requests
from bs4 import BeautifulSoup

author = 'Eko SW'
date = '1 November 2022'
url = 'https://www.bmkg.go.id/'

result = requests.get(url)
result = BeautifulSoup(result.text, 'html.parser')
divTag = result.find("span", {"class": "waktu"})
latest_earthquake = divTag.string
print(latest_earthquake)
