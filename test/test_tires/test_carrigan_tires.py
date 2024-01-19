import unittest

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_sensor = [0.8, 0.7, 0.9, 0.6]
        tires = CarriganTires(tire_wear_sensor)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear_sensor = [0.8, 0.8, 0.8, 0.7]
        tires = CarriganTires(tire_wear_sensor)
        self.assertFalse(tires.needs_service())
