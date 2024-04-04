import requests
from bs4 import BeautifulSoup
import csv

def fetch_articles(url):
    articles = []
    response = requests.get(url)
    webpage = response.content
    soup = BeautifulSoup(webpage, 'html.parser')
    items = soup.find_all('tr', class_='athing')
    for item in items:
        title = item.find('a', class_='titlelink').get_text()
        link = item.find('a', class_='titlelink')['href']
        age = item.find_next_sibling('tr').find('span', class_='age').get_text()
        articles.append({'title': title, 'url': link, 'published': age})
    return articles

def save_articles_to_csv(articles, filename='articles.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'url', 'published'])
        writer.writeheader()
        for article in articles:
            writer.writerow(article)

if __name__ == "__main__":
    url = 'https://news.ycombinator.com'
    articles = fetch_articles(url)
    save_articles_to_csv(articles)
    print(f'Scraped {len(articles)} articles from {url}.')
