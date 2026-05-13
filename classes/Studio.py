from classes.Home import Home

class Studio(Home):
    def __init__(self):
        super().__init__(
            price=1200.00, 
            extra_room_price=None, 
            garage_price=250.00, 
            garage_vacancy_multiplier=60.0
        )