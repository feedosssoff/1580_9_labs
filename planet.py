class Planet:
    count = 0

    def __init__(self, name, radius, mass, distance, ptype):
        Planet.count += 1
        self.name = name
        self.__radius = radius
        self.__mass = mass
        self.distance = distance
        self.ptype = ptype
        print(f"Создана планета {self.name}")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            raise ValueError("Радиус должен быть положительным числом")

    @property
    def mass(self):
        return self.__mass
   
    @mass.setter
    def mass(self, value):
        if value > 0:
            self.__mass = value
        else:
            raise ValueError("Масса должна быть положительным числом")

    def __str__(self):
        return f"{self.name}:\nРадиус - {self.radius}\nМасса - {self.mass}\nРасстояние от Солнца - {self.distance}\nТип планеты - {self.ptype}"

    def __repr__(self):
        return f"Planet('{self.name}', {self.radius}, {self.mass}, {self.distance}, '{self.ptype}')"

    def __del__(self):
        print(f"Удаление {self.name}")

    def __copy__(self):
        return Planet(self.name, self.radius, self.mass, self.distance, self.ptype)

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.name == other.name

    def to_dict(self):
        return {
            "name": self.name,
            "radius": self.radius,
            "mass": self.mass,
            "distance": self.distance,
            "type": self.ptype
        }
