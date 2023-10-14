from flask import Flask, render_template
import request

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=efface3884d84534b9001578724c73e0"
    r = request.get(url).json()
    cases = {
        'articles' : r['articles']
    }
    return render_template("news.html", case = cases)

if __name__ == "__main__":
    app.run(debug = True)
