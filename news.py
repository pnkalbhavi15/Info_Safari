from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# URL to scrape
url = "https://news24online.com/"

def scrape_content(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.prettify()  # Get the entire HTML content

            return content

    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

@app.route('/')
def index():
    news_content = scrape_content(url)
    return render_template("news.html", news_content=news_content)

if __name__ == '__main__':
    app.run(debug=True)
