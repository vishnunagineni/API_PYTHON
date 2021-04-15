from flask import Flask,render_template,request,flash,redirect
import requests
import random
from googlesearch import search
from url_metadata import URLMetadataCache
from bs4 import BeautifulSoup
app=Flask(__name__)
app.config['SECRET_KEY']='vishnu@1234'
@app.route('/',methods=['GET','POST'])
def create_app():
    
    if request.method=='POST':
        query=request.form.get('query')
        if len(query)>1:
            results=[]
            meta=[]
            for i in search(query,num=15,start=0,stop=15,pause=2.0):
                if i.find('glassdoor')==-1:
                    results.append(i)
                    url='https://google.com/search?q='+i
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text, 'lxml')
                    h=soup.find_all('h3')
                    print(h[0].get_text())
                    meta.append(h[0].text)
            return render_template('result.html',results=results,query=query,meta=meta)
        else:
            flash('Enter correct content to search')
    return render_template('home.html')
if __name__=="__main__":
    app.run(debug=True)
    