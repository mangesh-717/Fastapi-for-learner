import json

# Your data
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Specify the filename
filename = 'tempo.json'

# Write data to a JSON file
with open(filename, 'w') as file:
    json.dump(data, file, indent=4)

print(f'Data has been stored in {filename}')
