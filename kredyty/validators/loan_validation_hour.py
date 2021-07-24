from kredyty.load_json import ConfigData, ConfigDataNB
from datetime import datetime, timedelta

class LoanValidationHour():
    """Class used to validate loan properties."""
    def __init__(self, factor):
        self.factor = factor
        self.data = ConfigData().get_data()

    def validate(self):
        """Returns True if factors(dictionary) passed validations
        returns False if any propery didnt pass validations or none if no factors given."""
        min_hour = ConfigData().get_data()['min_hour']
        max_hour = ConfigData().get_data()['max_hour']
        if ( self.factor["hour"] < min_hour or self.factor["hour"] > max_hour):
            return False
        else:
            return True
