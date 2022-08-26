import requests
import json
from bs4 import BeautifulSoup

with open("1_movies.json","r") as f:
    a=json.load(f)
    i=0
    url=[]
    while i<len(a):
        print(i+1,":",a[i]["movie"])
        url.append(a[i]["link"])
        i=i+1
    user=int(input("Please enter the serial number:-"))-1
    x=url[user]
    b=requests.get(x)
    soup=BeautifulSoup(b.text,"html.parser")
    c=soup.find('script',type='application/ld+json').text
    a=json.loads(c)
    with open("TASK4_DETAILS.json","w") as f:
        json.dump(a,f,indent=2)
    with open("TASK4_DETAILS.json","r") as k:
        r=json.load(k)
    dic={}
    for j in r:
        dic['movie']=r['name']
        dic['director']=r['director'][0]['name']
        dic['image']=r['image']
        dic['description']=r['description']
        dic["language"]=r['review']['inLanguage']
        dic['genre']=r['genre']
        dic['Runtime']=r['duration']
        dic['country']='india'
    with open("TASK4.json","w") as f:
        json.dump(dic,f,indent=4)
        print(r)