import json
with open("task5.json","+r")as f:
    f2=json.load(f)
var=f2[:100]
def analyse_movies_language():
    list=[]
    for data in var:
        for key in data.keys():
            if key=="Language":
                for lang in data[key] :
                    if lang[0]!="(" and lang[-1]!=")":
                        if lang not in list:
                            list.append(lang)
    dict={}
    for l in list:
        c=0
        for ff in var:
            for k in ff.keys():
                if k=="Language":
                    for j in ff[k] :
                        if j==l:
                            c+=1
        dict[l]=c
    with open ("task6.json","w+")as f:
        file6=json.dump(dict,f,indent=6)
        return dict
analyse_movies_language()
