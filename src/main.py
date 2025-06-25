from car_park import CarPark
from sensor import ExitSensor, EntrySensor
from display import Display
from pathlib import Path

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark("moondalup", 100,None,None, None,"moondalup.txt")

# TODO: Write the car park configuration to a file called "moondalup_config.json"
car_park.write_config()
p = Path("config.json")
p.rename(Path(p.parent, "moondalup_config.json"))

# TODO: Reinitialize the car park object from the "moondalup_config.json" file
car_park = CarPark.from_config("moondalup_config.json")

# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(1,True,car_park)

# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(2,True,car_park)

# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(1, "Welcome to Moodalup", True, car_park)

# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for car in range(10):
    entry_sensor.update_car_park(f"1PPP0{car}")

# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for car in range(2):
    exit_sensor.update_car_park(f"1PPP0{car}")