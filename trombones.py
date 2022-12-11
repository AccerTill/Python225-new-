# # file # 2
#
# from bs4 import BeautifulSoup
# import requests
# import csv
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def write_csv(data):
#     with open('trombones.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'],
#                         data['url'],
#                         ))
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("div", class_="title")
#     # print("elements: ", elements )
#     for el in elements:
#         try:
#             name = el.find('a').text
#             print("name :", name)
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find("a").get('href')
#             print("URL: ", url)
#         except ValueError:
#             url = ''
#
#         data = {
#             'name': name,
#             'url': url,
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(2, 4):
#         print("-------- i:", i)
#         url = f"https://www.muztorg.ru/category/trombony?in-stock=1&pre-order=2&page={i}"
#         get_data(get_html(url))
#
# if __name__ == '__main__':
#     main()



#--------------------------------------------

from bs4 import BeautifulSoup
import requests


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        trombones = self.html.find_all("div", class_="title")
        for item in trombones:
            name = item.find("a").text
            href = item.find('a').get('href')

            self.res.append({"name": name,
                             'href': href})
        # print("RESULT: ", self.res)
        for i in self.res:
            print("I ------:", i)

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f"Name: {item['name']}\n"
                        f'Link: {item["href"]}'
                        f'\n\n{"*" * 20}\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
















