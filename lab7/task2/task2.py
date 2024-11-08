import json

file_path = 'ex_2.json'

with open(file_path) as f:
    data = json.load(f)
for i in data:
    print('name - ' + i['name'] + ', phoneNumber - ' + i['phoneNumber'])