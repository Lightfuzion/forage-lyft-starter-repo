from battery.battery import Battery
from utils import add_years_to_date


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.years_to_service = 4

    def needs_service(self) -> bool:
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, self.years_to_service)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
