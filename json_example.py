import json

user1={
    "username":"yerassyl",
    "age":22
}
user2={
    "username":"123",
    "age":2
}
user3={
    "username":"456",
    "age":50
}
arr=[]
arr.append(user1)
arr.append(user2)
arr.append(user3)
#соединение с файлом и запись json
with open("main.json","w") as file:
    json.dump(arr,file,indent=5)