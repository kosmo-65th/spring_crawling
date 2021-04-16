from flask import Flask, render_template,request
app = Flask(__name__)

# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup

import crawling

@app.route('/')
def hello():
    crawling.hongmoon()
    crawling.oralce_test()

    return render_template("index.html")

if __name__ == '__main__':
    app.run()