class Display:

    def __init__(self, id, message = "", is_on = False, car_park = None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        """Return the display's message"""
        return(f"Display {self.id}: {self.message}")

    def update(self, data):
        """Update displays values"""
        for key, value in data.items():
            if key == "message":
                self.message = value
            elif key == "is_on":
                self.is_on = value
            print(f"{key}: {value}")