from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location="Unknown", capacity=100, plates = None, displays = None, sensors = None):

        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []

    def __str__(self):
        return(f"Car park at {self.location}, with capacity {self.capacity}.")

    def register(self, component):
        if not isinstance(component, ( Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display.")
        else:
            if isinstance(component,Sensor):
                self.sensors.append(component)
            elif isinstance(component,Display):
                self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 25
        }
        for display in self.displays: display.update(data)

    @property
    def available_bays(self):
        if len(self.plates) >= self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)

