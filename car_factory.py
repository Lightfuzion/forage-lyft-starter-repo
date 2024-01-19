from car import Car


class CarFactory():
    def __init__(self):
        pass


    def create_calliope(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car()


    def create_glissade(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car()


    def create_palindrome(self, current_date, last_service_date, warning_light_on: bool) -> Car:
        return Car()


    def create_rorschach(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car()


    def create_thovex(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car()