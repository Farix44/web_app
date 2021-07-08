import json
import os
from load_json import ConfigData

# jj = str()
# with open('kredyty_config.json', 'r') as f:
# 	jj = f.read()
#
# data = json.loads(jj)
#
# min_godz = data['min_godzina']
# max_godz = data['max_godzina']
# print(type(data))
# print(data)
# print(type(data))
# print(type(data['min_godzina']))
# print(os.path.dirname('kredyty_config.json'))
# print(os.path.join('kredyty', 'kredyty_config.json'))

# c = ConfigData()
# value = c.get_data()['max_godzina']
# print(value)
print(ConfigData().get_data()['min_godzina'])
c = ConfigData()
print(c.get_data())
