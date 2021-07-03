import requests
import time
from bs4 import BeautifulSoup

url = "https://global.amo.go.kr/obsMetar/SearchObsMetarList.do?tm=9999.12.31%2023:59"

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
metar_soup = soup.select("#contentsTb tbody td:-soup-contains(METAR)")

metar_map = {}

for td in metar_soup:
    metar = " ".join(td.get_text().strip().split())
    airport = metar.split(" ")[1]
    metar_map[airport] = {'metar': metar, 'runway': []}

print(metar_map)
