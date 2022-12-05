import requests
from bs4 import BeautifulSoup
import lxml
import csv

url ="https://shop-avallon.ru/catalog/wind-instruments/saksofony/" \
     "?utm_source=none&utm_medium=cpc&utm_campaign=74234833&utm_content=premium.2&utm_term=" \
     "---autotargeting&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3NDIzNDgzMzsxMjc3MTY4MDQwMDt5YW5kZXgucnU6c" \
     "HJlbWl1bQ&yclid=11910330624978452479"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")


def write_csv(data):
    with open('Saxophones.csv', 'a') as f:
        writer = csv.writer(f, lineterminator = '\n', delimiter=';')
        writer.writerow((data['name'], data['url'], data['rating']))

d=[]
s=soup.find('div', class_='tpl-block-list-objects tpl-block-492-list')\
    .find_all('a', class_="main__hits-card-title")
# print(s)
for i in s:
    print(i.text)









