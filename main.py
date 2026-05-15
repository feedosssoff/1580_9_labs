from car import Car
from car_db import CarDB
from planet import Planet
from planet_db import PlanetDB

def valid_int(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] == "-":
        s = s[1:]
    return s.isdigit()

def valid_float(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] == "-":
        s = s[1:]
    if "." in s:
        ps = s.split(".")
        if len(ps) != 2:
            return False
        return ps[0].isdigit() and ps[1].isdigit()
    return s.isdigit()

def input_int(s):
    while True:
        info = input(s).strip()
        if valid_int(info):
            return int(info)
        print("ошибка ввода, нужно ввести целое число")

def input_float(s):
    while True:
        info = input(s).strip()
        if valid_float(info):
            return float(info)
        print("ошибка ввода, нужно ввести число")

def manage_planets(planet_db):
    while True:
        print("\nменю работы с планетами")
        print("1 загрузить базу из файла")
        print("2 сохранить базу в файл")
        print("3 вывести все записи на экран")
        print("4 добавить новую планету")
        print("5 найти планеты по фильтру")
        print("6 редактировать существующую запись")
        print("7 удалить планету из базы")
        print("8 сортировать записи")
        print("9 скопировать планету по индексу")
        print("10 экспортировать таблицу в csv")
        print("0 вернуться в главное меню")

        choice = input("выбери действие: ").strip()

        if choice == "1":
            planet_db.load()
        elif choice == "2":
            planet_db.save()
        elif choice == "3":
            planets = planet_db.get()
            if len(planets) == 0:
                print("в базе нет ни одной записи")
            else:
                print("список всех планет:")
                for idx in range(len(planets)):
                    curr_planet = planets[idx]
                    print(f"индекс {idx} - {curr_planet}")
        elif choice == "4":
            name = input("введи название планеты: ").strip()
            radius = input_float("введи радиус планеты: ")
            mass = input_float("введи массу планеты: ")
            distance = input_float("введи расстояние от солнца: ")
            p_type = input("введи тип планеты: ").strip()

            new = Planet(name, radius, mass, distance, p_type)
            planet_db.add(new)
        elif choice == "5":
            field = input("введи имя поля для поиска (name, radius, mass, distance, type): ").strip()
            value = input("введи значение для поиска: ").strip()
            res = planet_db.search(field, value)
            if len(res) > 0:
                print("найденные совпадения:")
                for idx in range(len(res)):
                    print(res[idx])
            else:
                print("по данному запросу ничего не найдено")
        elif choice == "6":
            




def main():
    planet_db = PlanetDB("planets.json")
    car_db = CarDB("cars.json")

    while True:
        print("\nглавное меню")
        print("1 база данных планет")
        print("2 база данных машин")
        print("0 выйти из программы")

        mainchoice = input("выбери пункт меню: ")

        if mainchoice == "1":
            manage_planets(planet_db)
        elif mainchoice == "2":
            manage_cars(car_db)
        elif mainchoice == "0":
            print("программа завершила работу")
            break
        else:
            print("ошибка: неверный выбор, попробуй еще раз")

if __name__ == "__main__":
    main()
        