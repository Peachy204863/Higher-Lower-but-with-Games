import requests
from bs4 import BeautifulSoup


pc_url = 'https://www.pricecharting.com/console/nintendo-64?sort=highest-price&genre-name=&exclude-variants=true&exclude-hardware=true&when=none&release-date=2022-11-17'
html_text = requests.get(pc_url).text
soup = BeautifulSoup(html_text, 'html.parser')

for link in soup.find_all("td",'title'):
    print(link.a.text)