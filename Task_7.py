import json

with open("TASK5.json","r") as f:
    a=json.load(f)
count={}
d1=[]
i=0
while i <len(a):
    if a[i]["director"]in count:
        count[a[i]["director"]]+=1
    else:
        count[a[i]["director"]]=1
    i=i+1
with open ("TASK7.json","w") as k:
    json.dump(count,k,indent=2)