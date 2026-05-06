class Car:
    count = 0

    def __init__(self, brand, model, year, vin, color, mileage):
        Car.count += 1
        
        self.brand = brand
        self.model = model
        self.year = year
        self.vin = vin
        self.color = color
        self.mileage = mileage
        
        print(f"Создан автомобиль: {self.brand} {self.model}")

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if value >= 1886 and value <= 2026:
            self.__year = value
        else:
            raise ValueError("Год выпуска должен быть между 1886 и 2026")

    @property
    def mileage(self):
        return self.__mileage
    
    @mileage.setter
    def mileage(self, value):
        if value >= 0:
            self.__mileage = value
        else:
            raise ValueError("Пробег не может быть отрицательным")

    def __str__(self):
        return f"{self.vin}: {self.brand} {self.model}, {self.year}г., {self.color}, {self.mileage}км"

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.year}, '{self.vin}', '{self.color}', {self.mileage})"

    def __del__(self):
        print(f"Удаление {self.vin}")

    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.vin == other.vin

    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "vin": self.vin,
            "color": self.color,
            "mileage": self.mileage
        }
