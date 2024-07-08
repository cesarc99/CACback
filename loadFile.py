# Python program to read
# json file

import json

# Opening JSON file
f = open('users.db')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list

print("Contenido")

for x in data:
    print(x["NomApe"].decode('utf-8'))

# print(data.encode('latin-1'))

# Closing file
f.close()
