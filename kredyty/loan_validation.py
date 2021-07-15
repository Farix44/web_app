from .load_json import ConfigData, ConfigDataNB

class LoanValidation:
    """Class used to validate loan properties."""
    def __init__(self, factors):
        self.factors = factors
        self.data = ConfigData().get_data()

    def validate(self):
        """Returns True if factors passed validations
        returns False if any propery didnt pass validations or none if no factors given."""
        for i in self.factors:
            if i == "godzina":
                min_godz = ConfigData().get_data()['min_godzina']
                max_godz = ConfigData().get_data()['max_godzina']
                if ( self.factors[i] < min_godz or self.factors[i] > max_godz):
                    return False
                else:
                    return True
            return False
