import time
import random
import os.path
from Task1 import movieData
var=movieData()
v=var[:10]
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
                        second=random.randint(0,3)
                        print(second)
                        time.sleep(second)
                        text=str(i)
                        data=f.write(text)
cache_file()