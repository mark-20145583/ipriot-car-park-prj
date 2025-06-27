from car_park import CarPark
from sensor import ExitSensor, EntrySensor
from display import Display
from pathlib import Path

car_park = CarPark("moondalup", 100,None,None, None,"moondalup.txt")

car_park.write_config()
p = Path("config.json")
p.rename(Path(p.parent, "moondalup_config.json"))

car_park = CarPark.from_config("moondalup_config.json")

entry_sensor = EntrySensor(1,True,car_park)

exit_sensor = ExitSensor(2,True,car_park)

display = Display(1, "Welcome to Moodalup", True, car_park)

for car in range(10):
    entry_sensor.update_car_park(f"1PPP0{car}")

for car in range(2):
    exit_sensor.update_car_park(f"1PPP0{car}")