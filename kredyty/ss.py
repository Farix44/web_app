import json
import os

jj = str()
with open('kredyty_config.json', 'r') as f:
	jj = f.read()

data = json.loads(jj)
# print(data)
# print(type(data))
# print(type(data['min_godzina']))

print(os.path.dirname('kredyty_config.json'))

print(os.path.join('kredyty', 'kredyty_config.json'))

