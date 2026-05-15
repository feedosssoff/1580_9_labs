import json
import os
from planet import Planet
import csv

class PlanetDB:
    def __init__(self, filename="planets.json"):
        self.filename = filename
        self.planets = list()

    def load(self):
        if not os.path.exists(self.filename):
            print("нет такого файла")
            return False

        self.planets.clear()
        Planet.counter = 0
        with open(self.filename, "r", encoding="utf-8") as file:
            info = json.load(file)
            for p in info:
                self.planets.append(Planet.from_dict(p))
            
        print("БД загружена")
        return True

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([p.to_dict() for p in self.planets], file, ensure_ascii=False, indent=4)

        print("БД сохранена")
        return True

    def add(self, planet):
        if isinstance(planet, Planet):
            self.planets.append(planet)
            print("планета добавлена")
            return True

        print("объект не экземпляр класса Planet")
        return False

    def remove(self, idx):
        if idx >= 0 and idx < len(self.planets):
            delete_object = self.planets.pop(idx)
            del delete_object
            return True
        return False

    def edit(self, idx, name, radius, mass, distance, p_type):
        if idx >= 0 and idx < len(self.planets):
            if name:
                self.planets[idx].name = str(name)
            if radius or radius == 0:
                self.planets[idx].radius = float(radius)
            if mass or mass == 0:
                self.planets[idx].mass = float(mass)
            if distance or distance == 0:
                self.planets[idx].distance = float(distance)
            if p_type:
                self.planets[idx].type = str(p_type)
            return True
        return False
    
    def get(self):
        return self.planets

    def search(self, field, value):
        res = list()
        strvalue = str(value).lower()
        for p in self.planets:
            if field == "name" and strvalue in p.name.lower():
                res.append(p)
            elif field == "radius" and str(p.radius) == strvalue:
                res.append(p)
            elif field == "mass" and str(p.mass) == strvalue:
                res.append(p)
            elif field == "distance" and str(p.distance) == strvalue:
                res.append(p)
            elif field == "type" and strvalue in p.type.lower():
                res.append(p)
            else:
                print("такого поля не существует")
                return False
        return res

    def selection_sort(self):
        length = len(self.planets)
        for i in range(length-1):
            min_index = i
            for j in range(i+1, length):
                if self.planets[j] < self.planets[min_index]:
                    min_index = j
                
            if min_index != i:
                self.planets[i], self.planets[min_index] = self.planets[min_index], self.planets[i]

    def bubble_sort(self):
        length = len(self.planets)
        for i in range(length-1):
            swapped = False
            for j in range(length-i-1):
                if self.planets[j] > self.planets[j+1]:
                    self.planets[j], self.planets[j+1] = self.planets[j+1], self.planets[j]
                    swapped = True
            
            if not swapped:
                break

    def insertion_sort(self):
        length = len(self.planets)
        for i in range(1, length):
            value = self.planets[i]
            j = i-1
            while j >= 0:
                if self.planets[j] > value:
                    self.planets[j+1] = self.planets[j]
                    j -= 1
                else:
                    break
            self.planets[j+1] = value

    def sort(self, field, algo):
        fields = ["name", "radius", "mass", "distance", "type"]
        if field in fields:
            Planet.mode = field
            if algo == "selection":
                self.selection_sort()
            elif algo == "bubble":
                self.bubble_sort()
            elif algo == "insertion":
                self.insertion_sort()
            else:
                print("алгоритм сортировки введен неверно")
                return False
            return True
        return False

    def export_csv(self, csv_file):
        fields = ["name", "radius", "mass", "distance", "type"]
        with open(csv_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for p in self.planets:
                writer.writerow(p.to_dict())
        return True