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

    def add_car(self):
        pass

    def remove_car(self):
        pass

    def update_displays(self):
        pass