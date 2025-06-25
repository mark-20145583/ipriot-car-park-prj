import unittest

from car_park import CarPark
from sensor import Sensor

class TestSensor(Sensor):

    def update_car_park(self, plate):
        return True



def test_sensor():

    try:
        car_park = CarPark("123 Example Street", 100)
        sensor = TestSensor(1,True,car_park)
        print("Test successful.")
    except:
        print("An error occurred")




