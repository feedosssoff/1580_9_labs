from functools import total_ordering

@total_ordering
class Car:
    counter = 0
    mode = "brand"
    def __init__(self, brand, model, year, vin, color, mileage):
        Car.counter += 1
        self.id = Car.counter

        self.brand = str(brand) if brand != "" else "none"
        self.model = str(model) if model != "" else "none"
        self.year = int(year) if isinstance(year, (float, int)) else 1886
        self.vin = str(vin) if vin != "" else "none"
        self.color = str(color) if color != "" else "none"
        self.mileage = float(mileage) if isinstance(mileage, (float, int)) else 0.0

        print(f"Создание ID {self.id}")

    def __del__(self):
        print(f"Удаление ID {self.id}")

    def __str__(self):
        return f"Автомобиль {self.brand} {self.model}: {self.year}г.в., VIN: {self.vin}, цвет: {self.color}, пробег: {self.mileage}"

    def __copy__(self):
        return Car(self.brand, self.model, self.year, self.vin, self.color, self.mileage)

    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented

        if Car.mode == "brand":
            return self.brand == other.brand
        elif Car.mode == "model":
            return self.model == other.model
        elif Car.mode == "year":
            return self.year == other.year
        elif Car.mode == "vin":
            return self.vin == other.vin
        elif Car.mode == "color":
            return self.color == other.color
        elif Car.mode == "mileage":
            return self.mileage == other.mileage
        return self.brand == other.brand

    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented

        if Car.mode == "brand":
            return self.brand < other.brand
        elif Car.mode == "model":
            return self.model < other.model
        elif Car.mode == "year":
            return self.year < other.year
        elif Car.mode == "vin":
            return self.vin < other.vin
        elif Car.mode == "color":
            return self.color < other.color
        elif Car.mode == "mileage":
            return self.mileage < other.mileage
        return self.brand < other.brand

    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "vin": self.vin,
            "color": self.color,
            "mileage": self.mileage
        }

    @classmethod
    def from_dict(cls, info):
        if isinstance(info, dict):
            return cls(
                info.get("brand", "none"),
                info.get("model", "none"),
                info.get("year", 1886),
                info.get("vin", "none"),
                info.get("color", "none"),
                info.get("mileage", 0.0)
            )
        return cls("none", "none", 1886, "none", "none", 0.0)