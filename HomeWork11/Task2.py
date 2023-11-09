import json

data = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}

with open('db.json', 'w') as file:
    json.dump(data, file, indent=4)


with open('db.json', 'r') as file:
    data = json.load(file)

print(data)