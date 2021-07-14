import json
import os

class ConfigData:
    """Class used for loading properties from kredyty-config.json for django build in files."""
    def __init__(self,):
        self.json_data = {}
        self.read_json()

    def read_json(self):
        try:
            with open(os.path.join('kredyty', 'kredyty_config.json'), 'r') as f:
                json_string = f.read()
            self.json_data = json.loads(json_string)
        except Exception as ex:
            print("Nie udalo sie wczytac 'kredyty_config.json' ")

    def get_data(self):
        return self.json_data

class ConfigDataNB:
    """Class used for loading properties from kredyty-config.json for user created files."""
    def __init__(self,):
        self.json_data = {}
        self.read_json()

    def read_json(self):
        try:
            with open(os.path.join('kredyty_config.json'), 'r') as f:
                json_string = f.read()
            self.json_data = json.loads(json_string)
        except Exception as ex:
            print("Nie udalo sie wczytac 'kredyty_config.json' ")

    def get_data(self):
        return self.json_data
