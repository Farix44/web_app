import json
import os
from load_json import ConfigData, ConfigDataNB
# from loan_validation import LoanValidation
from datetime import datetime, timedelta

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
# print(ConfigData().get_data()['min_godzina'])
# c = ConfigData()
# print(c.get_data())


# data = ConfigDataNB().get_data()
# print(data)

# for i in data:
#     print(i, data[i])

# curr_time = datetime.now() + timedelta(hours = ConfigDataNB().get_data()['roznica_czasu_godz'])   # timedelta - poprawka roznicy czasu
# f_dict = {"godzina": curr_time.hour}
# a = LoanValidation(f_dict)
# print(a.validate())

# curr_time = datetime.now() + timedelta(hours = ConfigDataNB().get_data()['roznica_czasu_godz'])   # timedelta - poprawka roznicy czasu
# factors = {}
# factors["godzina"] = curr_time.hour
# print(LoanValidation(factors).validate())

data = ConfigDataNB()
print(data.json_data)

# push test

# TO DO:
# (DONE) zmienne na angielski
# (DONE) valid klasa
# testy  ( ./manage.py test )
# (DONE) przeczytac artykuly
# wzorce projektowe w django
# doczytac jak dziala button submit z kodem z views.py
# stackoverflow spytac o podawanie sciezki do pliku
# (DONE) dodac komentarze do klas
