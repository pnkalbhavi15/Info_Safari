from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# List of URLs of tech-related websites to scrape
websites = [
    "https://news24online.com/"
]

def scrape_headings(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headings = soup.find_all(['h1', 'h2'])

            # Extract the heading text
            heading_texts = [heading.text for heading in headings]

            return heading_texts
        else:
            return [f"Failed to retrieve the web page from {url}. Status code: {response.status_code}"]
    except Exception as e:
        return [f"An error occurred while scraping {url}: {str(e)}"]

@app.route('/')
def index():
    all_headings = []
    for website in websites:
        headings = scrape_headings(website)
        all_headings.extend(headings)
    return render_template('news_1.html', headings=all_headings)

if __name__ == '__main__':
    app.run(debug=True)