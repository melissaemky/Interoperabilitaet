import json
filename = 'your_file.json'
entry = {'carl': 33}
# 1. Read file contents
with open(filename, "r") as file:
    data = json.load(file)
# 2. Update json object
data.append(entry)
# 3. Write json file
with open(filename, "w") as file:
    json.dump(data, file)