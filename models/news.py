import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import date, timedelta, datetime
import re

# Replace 'html_content' with your HTML content
#html_content = "<html>...</html>"

# Create a BeautifulSoup object with the 'html.parser' parser
#soup = bs(html_content, 'html.parser')

article_headlines = []
article_timestamps = []

ticker = 'AMC'
date = date.today()
days = 50

for i in range(days):
    year, month, day = str(date).split('-')

    url = f"https://www.marketwatch.com/search?q={ticker}&ts=5&sd={month}%2F{day}%2F{year}&ed={month}%2F{day}%2F{year}&tab=All%20News"

    response = requests.get(url)
    html = response.text
    soup = bs(html,features="html.parser")

    for div in soup.findAll('div', attrs={'class':'article__content'})[:-1]:
        article_headlines.append(div.find('a', attrs={'class':'link'}).text.strip())
        article_timestamps.append(div.find('span', attrs={'class':'article__timestamp'}))

    date = date - timedelta(days=1)

for i,v in enumerate(article_timestamps):
    if v is None:
        continue

    article_timestamps[i] = v.attrs['data-est'].replace('T',' ')

df = pd.DataFrame({"Headline": article_headlines, "Timestamp": article_timestamps})
df = df.drop_duplicates().dropna(axis=0,how='any')
pd.to_datetime(df['Timestamp'])
df.to_csv('out.csv')