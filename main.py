import planet
import json

output = "planets.json"

def save():
    info = list()
    for p in planets:
        info.append(p.transform())

    with open(output, "w", encoding="utf-8") as file:
        json.dump(info, file, indent=4, ensure_ascii=False)
    
def load():
    with open(output, "r", encoding="utf-8") as file:
        info = json.load(file)
        plist = []
        for object in info:
            p = planet.Planet(
                object["Имя планеты"],
                object["Радиус"],
                object["Масса"],
                object["Расстояние от Солнца"],
                object["Тип планеты"])
            plist.append(p)
        return plist

planets = load()

while True:
    print()
    print("1: Сортировать")
    print("2: Добавить")
    print("3: Удалить")
    print("4: Редактировать")
    print("5: Вывод на экран")
    print("exit: Выход")
    
    command = input()
    
    if command == "1":
        print("Выберите поле 1-имя 2-радиус 3-дистанция от солнца 4-масса")
        sort = input()
        if sort == "1":
            planets.sort(key=lambda x: x.name)
        elif sort == "2":
            planets.sort(key=lambda x: x.radius)
        elif sort == "3":
            planets.sort(key=lambda x: x.distance)
        elif sort == "4":
            planets.sort(key=lambda x: x.mass)
        
        save()
        print("выполнено")
        
    elif command == "2":
        name = input("Имя: ")
        
        rad = input("Введите радиус в км: ")
        if not rad.replace('.', '').isdigit():
            print("это не число")
            continue 
        radius = float(rad)
        if radius <= 0:
            print("радиус должен быть > 0")
            continue
        
        m = input("Введите массу в кг: ")
        if not m.replace('.', '').isdigit():
            print("это не число")
            continue
        mass = float(m)
        if mass <= 0:
            print("масса должна быть > 0")
            continue
        
        dist = input("Введите расстояние в млн км: ")
        if not dist.replace('.', '').isdigit():
            print("это не число")
            continue
        distance = float(dist)
        if distance <= 0:
            print("расстояние должно быть > 0")
            continue
        
        type = input("Тип каменная/газовый гигант/ледяной гигант: ").lower().strip()
        if type not in ["каменная", "газовый гигант", "ледяной гигант"]:
            print("неверный тип планеты")
            continue
        
        new_planet = planet.Planet(name, radius, mass, distance, type)
        planets.append(new_planet)
        save()
        print(f"Планета {name} добавлена")
        
    elif command == "3":
        print("Список планет:", end=" ")
        for p in planets:
            print(p.name, end=", ")
        print()
        
        delete = input("Введи имя планеты которую хочешь удалить: ")
        if delete == "":
            print("Ничего не введено")
            continue

        found = False
        for i in range(len(planets)):
            if planets[i].name.lower() == delete.lower():
                del planets[i]
                found = True
                save()
                print(f"Планета {delete} удалена")
                break
        
        if not found:
            print("Планета не найдена")
            
    elif command == "4":
        pass
    
    elif command == "5":
        for p in planets:
            print(f"{p.name}: радиус {p.radius}, масса {p.mass}")
    
    elif command == "exit":
        break