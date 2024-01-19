from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear
        self.service_tires_when_tire_at = 0.9

    def needs_service(self) -> bool:
        for item in self.tire_wear:
            if item >= self.service_tires_when_tire_at:
                return True
        return False
