import json
from task5 import srape_movie_details
var=srape_movie_details()
top_100=var[:10]
# print(top_100)
list=[]
def analyse_movies_language():
    for i in top_100:
        print(i["Language"])
        # list.append(i["Language"])

        # list=[]
        # # for j in i:
        # # print(i["Language"])
        # if i=="Language":
        #     print(i["Language"])
    #         list.append(i["language"])
    # print(list)



analyse_movies_language()

