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

def edit_str(s, curr):
    info = input(s).strip()
    if info == "":
        return curr
    return info

def edit_int(s, curr):
    while True:
        info = input(s).strip()
        if info == "":
            return curr
        if valid_int(info):
            return int(info)
        print("ошибка, введи целое число или оставь строку пустой")

def edit_float(s, curr):
    while True:
        info = input(s).strip()
        if info == "":
            return curr
        if valid_float(info):
            return float(info)
        print("ошибка, введи число или оставь строку пустой")

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

            if res is None:
                continue
            if len(res) > 0:
                print("найденные совпадения:")
                for idx in range(len(res)):
                    print(res[idx])
            else:
                print("по данному запросу ничего не найдено")

        elif choice == "6":
            planets = planet_db.get()
            if len(planets) == 0:
                print("база пуста, редактирование невозможно")
                continue
            print("доступные записи:")
            for idx in range(len(planets)):
                print(f"индекс {idx}: {planets[idx].name}")

            edit_idx = input_int("введи индекс для редактирования: ")

            if edit_idx >= 0 and edit_idx < len(planets):
                old = planets[edit_idx]
                print("если менять поле не нужно просто нажми enter")

                new_name = edit_str(f"новое имя [{old.name}]: ", old.name)
                new_radius = edit_float(f"новый радиус [{old.radius}]: ", old.radius)
                new_mass = edit_float(f"новая масса [{old.mass}]: ", old.mass)
                new_distance = edit_float(f"новая дистанция [{old.distance}]: ", old.distance)
                new_type = edit_str(f"новый тип [{old.type}]: ", old.type)

                planet_db.edit(edit_idx, new_name, new_radius, new_mass, new_distance, new_type)
                print("изменения сохранены")
            else:
                print("ошибка: неверный индекс")

        elif choice == "7":
            planets = planet_db.get()
            if len(planets) == 0:
                print("база пуста, удалять нечего")
                continue
            print("доступные записи:")
            for idx in range(len(planets)):
                print(f"индекс {idx}: {planets[idx].name}")
            
            delete_idx = input_int("введи индекс для удаления: ")

            if delete_idx >= 0 and delete_idx < len(planets):
                confirm = input("вы уверены, что хотите удалить эту запись? (да/нет): ").strip()
                if confirm == "да":
                    if planet_db.remove(delete_idx):
                        print("запись удалена")
                    else:
                        print("ошибка при удалении записи")
                else:
                    print("удаление отменено")
            else:
                print("ошибка: неверный индекс")

        elif choice == "8":
            field = input("введи поле для сортировки (name, radius, mass, distance, type): ").strip()
            algo = input("введи алгоритм (selection, bubble, insertion): ").strip()
            if planet_db.sort(field, algo):
                print("база данных отсортирована")
            else:
                print("ошибка: неверное поле или неизвестный алгоритм")

        elif choice == "9":
            planets = planet_db.get()
            if len(planets) == 0:
                print("база пуста, копирование невозможно")
                continue
            print("доступные записи:")
            for idx in range(len(planets)):
                print(f"индекс {idx}: {planets[idx].name}")

            copy_idx = input_int("введи индекс для копирования: ")

            if copy_idx >= 0 and copy_idx < len(planets):
                confirm = input("создать копию этого объекта? (да/нет): ").strip()
                if confirm == "да":
                    copied = planets[copy_idx].__copy__()
                    planet_db.add(copied)
                    print("дубликат объекта добавлен")
                else:
                    print("копирование отменено")
            else:
                print("ошибка: неверный индекс")
        
        elif choice == "10":
            filename = input("введи имя csv файла: ").strip()
            planet_db.export_csv(filename)
            print("данные успешно экспортированы")
        
        elif choice == "0":
            break
        
        else:
            print("ошибка: выбран неверный пункт меню")

def manage_cars(car_db):
    while True:
        print("\nменю работы с машинами")
        print("1 загрузить базу из файла")
        print("2 сохранить базу в файл")
        print("3 вывести все записи на экран")
        print("4 добавить новую машину")
        print("5 найти машины по фильтру")
        print("6 редактировать существующую запись")
        print("7 удалить машину из базы")
        print("8 сортировать записи")
        print("9 скопировать машину по индексу")
        print("10 экспортировать таблицу в csv")
        print("0 вернуться в главное меню")
        
        choice = input("выбери действие: ").strip()

        if choice == "1":
            car_db.load()

        elif choice == "2":
            car_db.save()

        elif choice == "3":
            cars = car_db.get()
            if len(cars) == 0:
                print("в базе нет ни одной записи")
            else:
                print("список всех машин:")
                for idx in range(len(cars)):
                    curr_car = cars[idx]
                    print(f"индекс {idx} - {curr_car}")

        elif choice == "4":
            brand = input("введи марку машины: ").strip()
            model = input("введи модель машины: ").strip()
            year = input_int("введи год выпуска: ")
            vin = input("введи vin код: ").strip()
            color = input("введи цвет машины: ").strip()
            mileage = input_float("введи пробег машины: ")
            
            new_car = Car(brand, model, year, vin, color, mileage)
            car_db.add(new_car)

        elif choice == "5":
            field = input("введи имя поля для поиска (brand, model, year, vin, color, mileage): ").strip()
            value = input("введи значение для поиска: ").strip()
            res = car_db.search(field, value)

            if res is None:
                continue
            if len(res) > 0:
                print("найденные совпадения:")
                for idx in range(len(res)):
                    print(res[idx])
            else:
                print("по данному запросу ничего не найдено")

        elif choice == "6":
            cars = car_db.get()
            if len(cars) == 0:
                print("база пуста, редактирование невозможно")
                continue
            print("доступные записи:")
            for idx in range(len(cars)):
                print(f"индекс {idx}: {cars[idx].brand} {cars[idx].model}")
                
            edit_idx = input_int("введи индекс для редактирования: ")

            if edit_idx >= 0 and edit_idx < len(cars):
                old = cars[edit_idx]
                print("если менять поле не нужно, просто нажми enter")
                
                new_brand = edit_str(f"новая марка [{old.brand}]: ", old.brand)
                new_model = edit_str(f"новая модель [{old.model}]: ", old.model)
                new_year = edit_int(f"новый год [{old.year}]: ", old.year)
                new_vin = edit_str(f"новый vin [{old.vin}]: ", old.vin)
                new_color = edit_str(f"новый цвет [{old.color}]: ", old.color)
                new_mileage = edit_float(f"новый пробег [{old.mileage}]: ", old.mileage)
                
                car_db.edit(edit_idx, new_brand, new_model, new_year, new_vin, new_color, new_mileage)
                print("изменения сохранены")
            else:
                print("ошибка: неверный индекс")

        elif choice == "7":
            cars = car_db.get()
            if len(cars) == 0:
                print("база пуста, удалять нечего")
                continue
            print("доступные записи:")
            for idx in range(len(cars)):
                print(f"индекс {idx}: {cars[idx].brand} {cars[idx].model}")

            delete_idx = input_int("введи индекс для удаления: ")
            
            if delete_idx >= 0 and delete_idx < len(cars):
                confirm = input("вы уверены, что хотите удалить эту запись? (да/нет): ").strip()
                if confirm == "да":
                    if car_db.remove(delete_idx):
                        print("запись удалена")
                    else:
                        print("ошибка при удалении записи")
                else:
                    print("удаление отменено")
            else:
                print("ошибка: неверный индекс")

        elif choice == "8":
            field = input("введи поле для сортировки (brand, model, year, vin, color, mileage): ").strip()
            algo = input("введи алгоритм (selection, bubble, insertion): ").strip()
            if car_db.sort(field, algo):
                print("база данных отсортирована")
            else:
                print("ошибка: неверное поле или неизвестный алгоритм")

        elif choice == "9":
            cars = car_db.get()
            if len(cars) == 0:
                print("база пуста, копирование невозможно")
                continue
            print("доступные записи:")
            for idx in range(len(cars)):
                print(f"индекс {idx}: {cars[idx].brand} {cars[idx].model}")

            copy_idx = input_int("введи индекс для копирования: ")

            if copy_idx >= 0 and copy_idx < len(cars):
                confirm = input("создать копию этого объекта? (да/нет): ").strip()
                if confirm == "да":
                    copied = cars[copy_idx].__copy__()
                    car_db.add(copied)
                    print("дубликат объекта добавлен")
                else:
                    print("копирование отменено")
            else:
                print("ошибка: неверный индекс")

        elif choice == "10":
            filename = input("введи имя csv файла: ").strip()
            car_db.export_csv(filename)
            print("данные успешно экспортированы")

        elif choice == "0":
            break

        else:
            print("ошибка: выбран неверный пункт меню")

def main():
    planet_db = PlanetDB("planets.json")
    car_db = CarDB("cars.json")

    while True:
        print("\nглавное меню")
        print("1 база данных планет")
        print("2 база данных машин")
        print("0 выйти из программы")

        mainchoice = input("выбери пункт меню: ").strip()

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
        