from Task1 import movieData
import json
var=movieData()
# print(var)
def group_by_year():
    main={}
    for i in var :
        list=[]
        year=i["year"]
        if year not in main:
            for j in var:
                if year==j["year"]:
                    list.append(j)
            main[year]=list
    
        with open ("task2.json","w+") as f:
            file_task2=json.dump(main,f,indent=4)
    return main 
group_by_year()




