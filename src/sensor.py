from abc import ABC, abstractmethod
import random


class Sensor(ABC):

    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        """Return sensor status"""
        return f"Sensor {self.id} active? {self.is_active}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        """For mock testing"""
        return 'FAKE-' + format(random.randint(0,999), "03d")

    def detect_vehicle(self):
        """When a vehile is detected by the sensor"""
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        """Update carpark upon vehicle entering"""
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):

    def _scan_plate(self):
        """For mock testing"""
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        """Update carpark upon vehicle exiting"""
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")