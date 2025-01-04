# Análise de Sentimento com Notícias
from textblob import TextBlob
from bs4 import BeautifulSoup
import requests

def fetch_news():
    url = "https://www.google.com/search?q=IBOV&tbm=nws"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [item.get_text() for item in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')]
