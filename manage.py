import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb+srv://danielelevn:3gnzOIgdh9mjH9KM@clusters.2m8qhmo.mongodb.net/?retryWrites=true&w=majority')
db = client['Scrape']
collection = db['webscrape']

r = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll('tr', class_='athing')

formatted_links = []

for link in links:
    data = {
        'id': link['id'],
        'title': link.find_all('td')[2].a.text,
        "url": link.find_all('td')[2].a['href'],
        "rank": int(link.find_all('td')[0].span.text.replace('.', ''))
    }
    formatted_links.append(data)

collection.insert_many(formatted_links)

client.close()
