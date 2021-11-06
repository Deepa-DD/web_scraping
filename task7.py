import json
with open ("task5.json","r+") as f:
    file=json.load(f)
var=file[:100]
def analyse_movies_directors():
    list=[]
    for i in var:
        for j in i["Director"]:
            if j not in list:
                list.append(j)
    print(list) 
    all_list=[]
    for x in var:
        for y in x["Director"]:
            all_list.append(y)
    print(all_list)
    dic={}
    for lit in list:
        c=0
        for main in (all_list):
            if lit==main:
                c+=1
        dic[lit]=c
    print(dic)
    with open ("task7.json","w+") as f:
        file=json.dump(dic,f,indent=6)


analyse_movies_directors()
