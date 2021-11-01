import requests
from bs4 import BeautifulSoup
import json
link=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
data=BeautifulSoup(link.text,"html.parser")
def movieData():
    list=[]
    x=0
    mainDiv=data.find("div",class_="body_main container")
    subDiv=mainDiv.find("table",class_="table")
    tr=subDiv.find_all("tr")
    for i in tr :
        dict={}
        td=i.find_all("td")      
        for j in td:
            title=i.find("a",class_="unstyled articleLink")["href"][3:]
            dict["tital"]=title
            rating=i.find("span",class_="tMeterScore").get_text()[:-1]
            dict["rating"]=float(rating)
            review=i.find("td",class_="right hidden-xs").get_text()
            year=i.find("a",class_="unstyled articleLink").get_text()[-5:-1]
            dict["year"]=int(year)
            rank=i.find("td",class_="bold").get_text()[:-1]
            dict["rank"]=int(rank)
            url="https://www.rottentomatoes.com/m/"+title
            dict["url"]=url
            if dict not in list:
                x+=1
                list.append(dict)
                dict["position"]=x
            with open ("task1.json","w+") as f:
                file=json.dump(list,f,indent=4)
    return list
movieData()

