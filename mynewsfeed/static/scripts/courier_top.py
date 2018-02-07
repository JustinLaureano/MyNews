import json
from bs4 import BeautifulSoup
from pprint import pprint
import requests

r = requests.get("http://thecourier.com")
data = r.text
soup = BeautifulSoup(data, "lxml")

news_list = []
title_list = []
url_list = []

my_links = soup.find(class_='flexslider')

for link in my_links.find_all('h2'):
    title_list.append(link.string)


for link in my_links.find_all('a'):
    url_list.append(link.get('href'))


for index, title in enumerate(title_list):
    new_dict = {"model": "mynewsfeed.CourierPost", "pk": index + 1, "fields":
        {"title": title, "url": url_list[index]}}
    news_list.append(new_dict)

pprint(news_list)
with open('../../fixtures/courier_top.json', 'w') as file:
    file.write(json.dumps(news_list))