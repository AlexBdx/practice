import json

with open("hey.json") as f:
    data = json.load(f)

print(data)
print(data[0])
print("Commit 1")
print("Commit 2")
print("Commit 3b")
print("Commit 5")