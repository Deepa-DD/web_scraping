import json
with open ("task5.json","r+") as f :
    data=json.load(f)
v=data[:100]
def analyse_language_and_directors(v):
    main={}
    for i in v :
        for director in i["Director"]:
            main[director]={}
    for i in range (len(v)):
        for key in main:
            if key in v [i]["Director"]:
                if v[i]=="Language":
                    for lang in v [i]["Language"]:
                        main[key][lang]=0
    for i in range (len(v)):
        for key in main:
            if key in v [i]["Director"]:
                if v[i]=="Language":
                    for lang in v [i]["Language"]:
                        main[key][lang]+=1
    with open("task10.json","w+") as f:
        file10=json.dump(main,f,indent=6)
analyse_language_and_directors(v)






















































   

