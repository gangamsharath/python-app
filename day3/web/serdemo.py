#Serialization
import requests,json

url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)
users=json.loads(response.text)
#print(users)
data=json.dumps(users,indent=2) #memory level serilization
#print(data)

#file level serilization
with open('users.json','w') as fw:
    json.dump(data,fw)
    print("file created")

#deserilization
with open("users.json",'r') as fr:
    data=json.load(fr)
    print(data)

