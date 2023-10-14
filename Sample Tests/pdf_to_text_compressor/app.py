from flask import Flask
from flask_gzip import Gzip

app = Flask(__name)
gzip = Gzip(app)

@app.route('/compressed')
@gzip.gzip_page
def compressed_content():
  return "This content is Gzipped."

if _name_ == '_main_':
  app.run()