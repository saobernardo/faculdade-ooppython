from classes.Home import Home

class Apartment(Home):
    def __init__(self):
        super().__init__(
            price=700.00, 
            extra_room_price=200.00, 
            garage_price=300.00, 
            garage_vacancy_multiplier=None
        )