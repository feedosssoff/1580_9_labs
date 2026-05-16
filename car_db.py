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
        with open(self.filename, "r", encoding="utf-8") as file:
            info = json.load(file)
            for c in info:
                self.cars.append(Car.from_dict(c))

        print("база машин загружена")
        return True

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([c.to_dict() for c in self.cars], file, ensure_ascii=False, indent=4)

        print("база машин сохранена")
        return True

    def add(self, car):
        if isinstance(car, Car):
            self.cars.append(car)
            print("машина добавлена")
            return True

        print("объект не экземпляр класса Car")
        return False

    def remove(self, idx):
        if idx >= 0 and idx < len(self.cars):
            delete_object = self.cars.pop(idx)
            del delete_object
            return True
        return False

    def edit(self, idx, brand, model, year, vin, color, mileage):
        if idx >= 0 and idx < len(self.cars):
            if brand:
                self.cars[idx].brand = str(brand)
            if model:
                self.cars[idx].model = str(model)
            if year:
                self.cars[idx].year = int(year)
            if vin:
                self.cars[idx].vin = str(vin)
            if color:
                self.cars[idx].color = str(color)
            if mileage or mileage == 0:
                self.cars[idx].mileage = float(mileage)
            return True
        return False

    def get(self):
        return self.cars

    def search(self, field, value):
        res = list()
        strvalue = str(value).lower()
        for c in self.cars:
            if field == "brand" and strvalue in c.brand.lower():
                res.append(c)
            elif field == "model" and strvalue in c.model.lower():
                res.append(c)
            elif field == "year" and strvalue == str(c.year):
                res.append(c)
            elif field == "vin" and strvalue in c.vin.lower():
                res.append(c)
            elif field == "color" and strvalue in c.color.lower():
                res.append(c)
            elif field == "mileage" and strvalue == str(c.mileage):
                res.append(c)
            else:
                print("такого поля не существует")
                return []
        return res
    
    def selection_sort(self):
        length = len(self.cars)
        for i in range(length-1):
            min_index = i
            for j in range(i+1, length):
                if self.cars[j] < self.cars[min_index]:
                    min_index = j
            
            if min_index != i:
                self.cars[i], self.cars[min_index] = self.cars[min_index], self.cars[i]

    def bubble_sort(self):
        length = len(self.cars)
        for i in range(length-1):
            swapped = False
            for j in range(length-i-1):
                if self.cars[j] > self.cars[j+1]:
                    self.cars[j], self.cars[j+1] = self.cars[j+1], self.cars[j]
                    swapped = True

            if not swapped:
                break

    def insertion_sort(self):
        length = len(self.cars)
        for i in range(1, length):
            value = self.cars[i]
            j = i-1
            while j >= 0:
                if self.cars[j] > value:
                    self.cars[j+1] = self.cars[j]
                    j -= 1
                else:
                    break
            self.cars[j+1] = value

    def sort(self, field, algo):
        fields = ["brand", "model", "year", "vin", "color", "mileage"]
        if field in fields:
            Car.mode = field
            if algo == "selection":
                self.selection_sort()
            elif algo == "bubble":
                self.bubble_sort()
            elif algo == "insertion":
                self.insertion_sort()
            else:
                return False
            return True
        return False

    def export_csv(self, csv_file):
        fields = ["brand", "model", "year", "vin", "color", "mileage"]
        with open(csv_file, "w", encoding="utf-8", newline="") as file:
            writeheader = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for c in self.cars:
                writer.writerow(c.to_dict())
        return True