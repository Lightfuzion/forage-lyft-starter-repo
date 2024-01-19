from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear
        self.service_tires_when_sum = 3

    def needs_service(self):
        return sum(self.tire_wear) >= self.service_tires_when_sum
