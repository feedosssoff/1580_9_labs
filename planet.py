from functools import total_ordering

@total_ordering
class Planet:
    counter = 0
    mode = "distance"

    def __init__(self, name, radius, mass, distance, p_type):
        Planet.counter += 1
        self.id = Planet.counter

        self.name = str(name) if name != "" else "none"
        self.radius = float(radius) if isinstance(radius, (int, float)) else 0.0
        self.mass = float(mass) if isinstance(mass, (int, float)) else 0.0
        self.distance = float(distance) if isinstance(distance, (int, float)) else 0.0
        self.type = str(p_type) if p_type != "" else "none"
        print(f"Создание ID {self.id}")

    def __del__(self):
        print(f"Удаление ID {self.id}")

    def __str__(self):
        return f"Планета {self.name}: Радиус - {self.radius} км, Масса - {self.mass} кг, Расстояние от Солнца - {self.distance} млн км, Тип - {self.type}"

    def __repr__(self):
        return f"Planet({self.name}, {self.radius}, {self.mass}, {self.distance}, {self.type})"

    def __copy__(self):
        return Planet(self.name, self.radius, self.mass, self.distance, self.type)

    def __eq__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented

        if Planet.mode == "name":
            return self.name == other.name
        elif Planet.mode == "radius":
            return self.radius == other.radius
        elif Planet.mode == "mass":
            return self.mass == other.mass
        elif Planet.mode == "distance":
            return self.distance == other.distance
        elif Planet.mode == "type":
            return self.type == other.type
        return self.name == other.name

    def __lt__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented

        if Planet.mode == "name":
            return self.name < other.name
        elif Planet.mode == "radius":
            return self.radius < other.radius
        elif Planet.mode == "mass":
            return self.mass < other.mass
        elif Planet.mode == "distance":
            return self.distance < other.distance
        elif Planet.mode == "type":
            return self.type < other.type
        return self.distance < other.distance

    def to_dict(self):
        return {
            "name": self.name,
            "radius": self.radius,
            "mass": self.mass,
            "distance": self.distance,
            "type": self.type
        }

    @classmethod
    def from_dict(cls, info):
        if isinstance(info, dict):
            return cls(
                info.get("name", "none"),
                info.get("radius", 0.0),
                info.get("mass", 0.0),
                info.get("distance", 0.0),
                info.get("type", "none")
            )
        return cls("none", 0.0, 0.0, 0.0, "none")