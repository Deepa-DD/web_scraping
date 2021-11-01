import json
from Task1 import movieData
from task4 import scrape_top_list
var1=movieData()
top_100=var1[:100]
def srape_movie_details():
    list=[]
    for i in top_100:
        for j in i:
            if j=="url":
                list.append(scrape_top_list(i["url"]))
    with open ("task5.json","w+") as f:
        file5=json.dump(list,f,indent=6)
    return list
srape_movie_details()








