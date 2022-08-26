import json

file=open("1_movies.json")
movies=json.load(file)
def group_by_year():
    dic={}
    for i in movies:
        movie_list=[]
        year=i["year"]
        if year not in dic:
            for j in movies:
                if year==j["year"]:
                    movie_list.append(j)
            dic[year]=movie_list
        # print(dic)
    with open("TASK2.json","w") as f:
        json.dump(dic,f,indent=8,sort_keys=True)
    # print(file)
group_by_year()