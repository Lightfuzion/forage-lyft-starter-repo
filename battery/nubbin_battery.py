from battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date
        
    def needs_service(self) -> bool:
        pass