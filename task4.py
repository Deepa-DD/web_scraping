import json
import requests
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/m/inside_out_2015"

def scrape_top_list(url):
    link=requests.get(url)
    data=BeautifulSoup(link.text,"html.parser")
    mainDiv=data.find("h1",class_="scoreboard__title").get_text()
    subDiv=data.find_all("li",class_="meta-row clearfix")
    dic={}
    dic["Movie Name"]=mainDiv
    dic["Movie url"]=url
    for i in subDiv:
        a=i.text
        b=a.split()       
        for i2 in b:
            if i2=="Rating:":
                dic["Rating"]=b[1]
            if i2=="Genre:":
                l=b
                l.remove("Genre:")
                dic["Gener"]=l
            if i2=="Original":
                l2=b
                l2.remove("Language:")
                l2.remove("Original")
                dic["Language"]=l2
            if "Director:" in a:
                l_d=[]
                d1=0
                while d1<len(b):
                    if d1==0:
                        d1+=1
                        continue
                    l_d.append(b[d1])
                    d1+=1
                str=""
                for a_d2 in l_d:
                    if a_d2 ==" ":
                        pass
                    else:
                        str+=a_d2
                spl=str.split(",")
                dic["Director"]=spl
            if i2=="Producer:":
                l4=b
            if i2=="Runtime:":
                f=b[1]
                j=b[2]
                f2=f[:-1]
                j2=j[:-1]
                time=(int(f2)*60)+int(j2)
                dic["Timeline"]=time
    with open ("task4.json","w+") as f:
        JsonFile=json.dump(dic,f,indent=7)
        return dic
scrape_top_list(url)



































