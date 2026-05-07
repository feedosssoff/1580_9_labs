from functools import total_ordering
import json

@total_ordering
class Planet:
    _count = 0
    def __init__(self, name, radius, mass, distance, planet_type):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.planet_type = planet_type

        self.__id = Planet._count
        Planet._count += 1
        print(f"Создание ID {self.__id}")

    def __str__(self):
        return f"ID {self.__id}, Планета {self.name}:\nРадиус: {self.radius}км\nМасса: {self.mass}кг\nРасстояние от Солнца: {self.distance}млн км\n Тип планеты: {self.planet_type}"

    def __repr__(self):
        return f"Planet({self.__id}, {self.name}, {self.radius}, {self.mass}, {self.distance}, '{self.planet_type}')"

    def __del__(self):
        print(f"Удаление ID {self.__id}")

    def __copy__(self):
        return Planet(self.name, self.radius, self.mass, self.distance, self.planet_type)

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
            "planet_type": self.planet_type
        }

    
