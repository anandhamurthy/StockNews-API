from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

global soup1


@app.route('/news',methods=['GET','POST'])
def news_search_transcriptdaily():
    url="https://transcriptdaily.com/markets"
    page = requests.get(url)
    soup1 = BeautifulSoup(page.content,'lxml')
    news=[]
    for item in soup1.findAll("div", {"class": "entry"}):
        for j in item.findAll('a'):
            t=j.text
            if t!='':
                t=t.replace('\n', '').replace('\t', '').replace('\r', '').replace('\xa0', '')
                href = j.get('href')
                n = {
                    "title": j.get('title'),
                    "text": t,
                    "a": href
                }
                news.append(n)
    return ({"news": news})




if __name__ == "__main__":
    app.run(debug=True)
