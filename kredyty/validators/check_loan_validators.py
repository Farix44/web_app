from kredyty.validators.loan_validation_hour import LoanValidationHour
from datetime import datetime, timedelta
from kredyty.load_json import ConfigData, ConfigDataNB

class CheckLoanValidators:
    def __init__(self):
        curr_time = datetime.now() + timedelta(hours = ConfigData().get_data()['time_zone_difference'])   # timedelta - poprawka roznicy czasu
        factors = {}
        factors["hour"] = curr_time.hour
        self.list = [LoanValidationHour(factors).validate()]

    def validate(self):
        for i in self.list:
            if i == False:
                return False
                break
        return True
