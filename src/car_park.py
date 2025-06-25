from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entr
import json

class CarPark:
    def __init__(self, location="Unknown", capacity=100, plates = None, displays = None, sensors = None, log_file=Path("log.txt")):

        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        """Return the locations current capacity."""
        return f"Car park at {self.location}, with capacity {self.capacity}."

    def write_config(self):
        """Save config to file"""
        with open("config.json","w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    def _log_car_activity(self, plate, action):
        """Record activity to log file"""
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def register(self, component):
        """Register either sensor or display to the carpark"""
        if not isinstance(component, ( Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display.")
        else:
            if isinstance(component,Sensor):
                self.sensors.append(component)
            elif isinstance(component,Display):
                self.displays.append(component)

    def add_car(self, plate):
        """Add a car to the carpark"""
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        """Remove a car from the carpark"""
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        """Update displays with accurate values"""
        data = {
            "available_bays": self.available_bays,
            "temperature": 25
        }
        for display in self.displays: display.update(data)

    @property
    def available_bays(self):
        """The number of bays available for use"""
        if len(self.plates) >= self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        """Load a carpark from a pre-set config file"""
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"],config["capacity"], log_file=config["log_file"])