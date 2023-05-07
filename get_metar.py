import requests
import time
import json
from bs4 import BeautifulSoup

url = "http://global.amo.go.kr/obsMetar/SearchObsMetarList.do?tm=9999.12.31%2023:59"

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
metar_soup = soup.select("#contentsTb tbody td:-soup-contains(METAR),td:-soup-contains(SPECI)")

metar_map = {} 

for td in metar_soup:
    metar = " ".join(td.get_text().strip().split())
    airport = metar.split(" ")[1]
    if airport == 'COR':
        airport = metar.split(" ")[2]
    if 'RK' in airport:
        metar_map[airport] = metar

print(json.dumps(metar_map))
