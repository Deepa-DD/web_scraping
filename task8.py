import os.path
import requests
from Task1 import movieData
var=movieData()
v=var[:100]
def cache_file():
    for i in v:
        for j in i:
            if j=="url":
                url=i["url"]
                name=i["tital"]
                file_name=str(name)+".txt"
                if os.path.exists(file_name):
                    pass
                else:
                    with open (file_name,"w+") as f:
                        request=requests.get(url)
                        data=f.write(request.text)
cache_file()