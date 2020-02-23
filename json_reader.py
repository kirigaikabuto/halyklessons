import json
arr=[]
with open("main.json","r") as file:
    arr = json.load(file)
for i in arr:
    print(i)