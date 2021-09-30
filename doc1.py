import json

with open("hey.json") as f:
    data = json.load(f)

print(data)
print(data[0])
print("Something")
