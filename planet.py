class Planet():
    total_planets = 0 
    def __init__(self, name, radius, mass, distance, type):
        self.name = name
        self.__radius = radius
        self.__mass = mass
        self.distance = distance
        self.__type = type
        Planet.total_planets += 1
        
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, rad):
        if rad > 0:
            self.__radius = rad
        else:
            raise ValueError("Радиус должен быть положительным числом")
        
    @property
    def mass(self):
        return self.__mass
    
    @mass.setter
    def mass(self, mas):
        if mas > 0:
            self.__mass = mas
        else:
            raise ValueError("Масса должна быть положительным числом")
            
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, value):
        if value in ["газовый гигант", "каменная", "ледяной гигант"]:
            self.__type = value
        else:
            raise ValueError("Тип должен быть 'газовый гигант', 'каменная' или 'ледяной гигант'")
        
    def transform(self):
        return {
            "Имя планеты": self.name,
            "Радиус": self.radius,
            "Масса": self.mass,
            "Расстояние от Солнца": self.distance,
            "Тип планенты": self.type
        }
    