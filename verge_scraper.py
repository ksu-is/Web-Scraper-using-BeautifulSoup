# Created by Norman McCord

# This is adapted from https://github.com/mfakharealam/Web-Scraper-using-BeautifulSoup. It is a scraper used to find the latest articles from TheVerge.com and export links to them to a csv file. 

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# fetch content
url = 'https://www.theverge.com'
html_source = requests.get(url).text
soup = BeautifulSoup(html_source, 'html.parser')

# find the article headlines and links
# articles = soup.find_all('h2', class_='inline-block', limit=10)
articles = soup.select('a[data-analytics-link="article"]')[:10]

# create the csv file
timestamp = datetime.now().strftime("%Y-%b-%d") # gives current date and time in 24-hour format for use in the filename
filename = f'theverge_headlines_{timestamp}.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Headline', 'URL']) # crates the headers in the csv file

    if not articles:
        print("No articles found. The page structure may have changed.")
    for article in articles:
        headline = article.get_text(strip=True)
        link = article['href']
        if not link.startswith('http'):
            link = f'https://www.theverge.com{link}'
        writer.writerow([headline, link])
        print(f"{headline} - {link}")
