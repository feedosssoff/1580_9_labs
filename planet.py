from functools import total_ordering
import json
import os

@total_ordering
class Planet:
    _counter = 0

    def __init__(self, name, radius, mass, distance, p_type):
        self.name = name
        self.radius = float(radius)
        self.mass = float(mass)
        self.distance = float(distance)
        self.p_type = p_type

        self.id = Planet._counter
        Planet._counter += 1
        print(f"Создание ID {self.id}")

    def __del__(self):
        print(f"Удаление ID {self.id}")

    def __str__(self):
        return f"{self.id} - Планета {self.name}: Радиус - {self.radius}км, Масса - {self.mass}кг, Расстояние от Солнца - {self.distance}млн км, Тип - {self.p_type}"

    def __repr__(self):
        return f"Planet({self.name}, {self.radius}, {self.mass}, {self.distance}, {self.p_type})"
    
    def __copy__(self):
        return Planet(self.name, self.radius, self.mass, self.distance, self.p_type)

    def __eq__(self, other):
        if isinstance(other, Planet):
            return self.name == other.name
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Planet):
            return self.distance < other.distance
        return NotImplemented

    def to_dict(self):
        return {
            "name": self.name,
            "radius": self.radius,
            "mass": self.mass,
            "distance": self.distance,
            "p_type": self.p_type
        }
    
    @classmethod
    def from_dict(cls, info):
        return cls(info["name"], info["radius"], info["mass"], info["distance"], info["p_type"])

class PlanetDB:
    def __init__(self, filename="planets.json"):
        self.filename = filename
        self.planets = list()

    def load(self):
        if not os.path.exists(self.filename):
            print("нет такого файла")
            return

        Planet._counter = 0
        with open(self.filename, 'r', encoding='utf-8') as file:
            info = json.load(file)
            self.planets = list()
            for p in info:
                self.planets.append(Planet.from_dict(p))

        print("БД згружена")

    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([p.to_dict() for p in self.planets], file, ensure_ascii=False, indent=4)
        print("БД сохранена")

    def add(self, planet):
        self.planets.append(planet)
        print("планета добавлена")

    def remove_name(self, name):
        delete = None
        for p in self.planets:
            if p.name.lower() == name.lower():
                delete = p
                break

        if delete:
            self.planets.remove(delete)
            print(f"планета {name} удалена")
            del delete
        else:
            print("нет такой планеты")

    def edit(self, name, new_name, new_radius, new_mass, new_distance, new_type):
        for p in self.planets:
            if p.name.lower() == name.lower():
                p.name = new_name
                p.radius = new_radius
                p.mass = new_mass
                p.distance = new_distance
                p.p_type = new_type
                print("данные обновлены")
                return
        print("планета не найдена")

    def display(self):
        if self.planets == []:
            print("БД пуста")
            return
        for p in self.planets:
            print(p)

    def sort(self, field):
        length = len(self.planets)
        for i in range(1, length):
            value = self.planets[i]
            j = i-1

            while j >= 0:
                curr = self.planets[j]
                swap = False

                if field == "distance":
                    if curr > value: swap = True
                elif field == "name":
                    if curr.name.lower() > value.name.lower(): swap = True
                elif field == "radius":
                    if curr.radius > value.radius: swap = True

                if swap:
                    self.planets[j+1] = self.planets[j]
                    j -= 1
                else:
                    break

            self.planets[j+1] = value

        print(f"БД отсортирована по {field}")