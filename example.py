import json

def adduser(u,p):
    arr=[]
    user={
    "username":u,
    "age":p
    }
    with open("main.json","r") as file:
        arr = json.load(file)
    arr.remove(user)
    with open("main.json","w") as file:
        json.dump(arr,file,indent=5)
    

adduser("yerassyl",123123)