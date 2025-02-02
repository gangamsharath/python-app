import pickle,json,requests

url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)
users=json.loads(response.text)

with open("users.pkl","bw") as filewriter:
    pickle.dump(users,filewriter)
    print("binary serlization is done")