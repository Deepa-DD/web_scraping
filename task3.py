import json 
with open ("task2.json","r+") as f:
    file=json.load(f)
def group_by_decade(a):
    year_list=[]
    movie_dic={}
    for i in a:
        if i not in year_list:
            mod=int(i)%10
            year=int(i)-mod
            year_list.append(year)
        year_list.sort()     
    for j in  year_list:
        movie_dic[j]=[]
    for d in  movie_dic:
        decate=d+9
        for i2 in a:
            if int(i2) <=decate and int(i2)>=d:
                for v in a[i2]:
                    movie_dic[d].append(a[i2])
    with open ("task3.json","w+") as f :
        file=json.dump(movie_dic,f,indent=4)
    return movie_dic
group_by_decade(file)






