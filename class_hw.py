class Auto:
    mileage = 0.0

    def __init__(self, brand: str, producer: str, fuel_consumption: float, year_created: int = 2020):
        self.year_created = year_created
        self.producer = producer
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return (f"Рік створення - {self.year_created} year\n "
                f"Виробник - {self.producer}\n "
                f"Бренд - {self.brand}\n "
                f"Витрата палива - {self.fuel_consumption}l\n "
                f"Пробіг - {self.mileage}km\n ")

    def signal_auto(self):
        print(" *klaxon_sound* ")


new_car = Auto(brand="mercedes", producer="Germany", fuel_consumption=100, year_created=2017)
new_car_2 = Auto(brand="fiat", producer="Italy", fuel_consumption=50, year_created=2009)

new_car_2.mileage = 35805.04
new_car.mileage = 10000

new_car.signal_auto()

print(new_car_2)
print(new_car)
