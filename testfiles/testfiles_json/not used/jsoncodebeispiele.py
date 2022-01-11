import json

# Convert json to dict
person = '{"name": "Bob", "languages": ["English", "Fench"]}'  # json string
# json dictionary, suppose: existing file: person.json which contains a json object
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])


# Open json dict
with open('path_to_file/person.json') as f:
    data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)

# Convert dict to json
person_dict = {'name': 'Bob',
               'age': 12,
               'children': None
               }
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)

# Write json to a file
person_dict = {"name": "Bob",
               "languages": ["English", "Fench"],
               "married": True,
               "age": 32
               }

with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)
