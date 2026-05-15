import json
import os
from car import Car
import csv

class CarDB:
    def __init__(self, filename="cars.json"):
        self.filename = filename
        self.cars = list()

    def load(self):
        if not os.path.exists(self.filename):
            print("нет такого файла")
            return False

        self.cars.clear()
        Car.counter = 0
        with open(self.filename, 'r', encoding='utf-8') as file:
            info = json.load(file)
            self.cars = list()
            for c in info:
                self.cars.append(Car.from_dict(p))

        print("БД загружена")
        return True

    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([c.to_dict() for c in self.cars], file, ensure_ascii=False, indent=4)

        print("БД сохранена")
        return True

    def add(self, car):
        if isinstance(car, Car):
            self.cars.append(car)
            print("планета добавлена")
            return True
        return False

    def remove(self, idx):
        if idx >= 0 and idx < len(self.cars):
            delete_object = self.cars.pop(idx)
            del delete_object
            return True
        return False
