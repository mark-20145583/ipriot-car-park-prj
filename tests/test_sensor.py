import unittest

from car_park import CarPark
from sensor import Sensor

class TestSensor(Sensor):

    def setUp(self):
         self.car_park = CarPark("123 Example Street", 100)

    def update_car_park(self, plate):
        return True

    def test_sensor(self):
        with self.assertRaises(ValueError)
            self.sensor = TestSensor(1,True,self.car_park)




