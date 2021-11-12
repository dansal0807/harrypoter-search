import requests
import json

session = requests.Session()
url = "http://hp-api.herokuapp.com/api/characters"
r = requests.get(url)
datas = json.loads(r.text)

for data in datas:
    name = data['name']
    gender = data['gender']
    house = data['house']
    actor = data['actor']

    if name == "Harry Potter":
        print(name, gender, house, actor)


