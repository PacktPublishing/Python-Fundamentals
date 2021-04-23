import json

with open('example.json') as f:
    data = json.loads(f.read())

print(data)
print(type(data))