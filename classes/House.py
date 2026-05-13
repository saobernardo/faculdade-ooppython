from classes.Home import Home

class House(Home):
    def __init__(self):
        super().__init__(
            price=900.00, 
            extra_room_price=250.00, 
            garage_price=300.00, 
            garage_vacancy_multiplier=None
        )