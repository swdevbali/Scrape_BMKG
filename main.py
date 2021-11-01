"""
This project will get the latest information about earthquake from bmkg.go.id
"""
author = 'Eko SW'
date = '1 November 2022'
url = 'https://www.bmkg.go.id/'

import requests
result = requests.get(url)
print(result.status_code)
print(result.text)

result = BeautifulSoup`