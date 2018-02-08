import json
from bs4 import BeautifulSoup
from pprint import pprint
import requests

r = requests.get("https://www.nytimes.com/")
data = r.text
soup = BeautifulSoup(data, "lxml")

top_news = soup.find(class_='top-news')
headlines = top_news.find_all('a')

news_list = []
unique_id = 1

for link in headlines[:10]:
    new_dict = {"model": "mynewsfeed.NYTimes", "pk": unique_id, "fields": {
        "title": link.string, "url": link.get('href')}}

    news_list.append(new_dict)
    unique_id += 1

pprint(news_list)
with open('../../fixtures/ny_times.json', 'w') as file:
    file.write(json.dumps(news_list))
