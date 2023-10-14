# Import necessary libraries
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Define a function to scrape Indian news
def scrape_indian_news():
    # Replace 'url' with the URL of the Indian news website you want to scrape
    url = 'https://example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract news articles
    news_articles = []
    for article in soup.find_all('div', class_='news-article'):
        title = article.find('h2').text
        content = article.find('p').text
        news_articles.append({'title': title, 'content': content})

    return news_articles

@app.route('/')
def index():
    # Call the scrape_indian_news function to get news articles
    news_articles = scrape_indian_news()
    return render_template('news.html', news_articles=news_articles)

if __name__ == '__main__':
    app.run(debug=True)
