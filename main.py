from planet import Planet
import json

def load():
    with open("planets.json", "r", encoding="utf-8") as f:
        items = json.load(f)
        res = []
        for i in items:
            res.append(Planet(i['name'], i['radius'], i['mass'], i['distance'], i['type']))
        return res

def save(planets):
    plist = list(p.to_dict() for p in planets)
    with open("planets.json", "w", encoding="utf-8") as f:
        json.dump(plist, f, indent=4, ensure_ascii=False)

def bubble_sort(arr, field):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if field == "name":
                v1, v2 = arr[j].name, arr[j+1].name
            elif field == "radius":
                v1, v2 = arr[j].radius, arr[j+1].radius
            elif field == "mass":
                v1, v2 = arr[j].mass, arr[j+1].mass
            elif field == "distance":
                v1, v2 = arr[j].distance, arr[j+1].distance
            else:
                return
            
            if v1 > v2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    planets = load()
    
    while True:
        print()
        print("1.Вывести все")
        print("2.Добавить планету")
        print("3.Удалить планету")
        print("4.Редактировать")
        print("5.Сортировка")
        print("6.Выход")
        
        choice = input("Выбор: ")

        if choice == "1":
            if not planets:
                print("ПУСТО!!!!")
            for p in planets:
                print(p)

        elif choice == "2":
            name = input("Название: ")
            radius = float(input("Радиус: "))
            mass = float(input("Масса: "))
            distance = float(input("Расстояние: "))
            ptype = input("Тип: ")
            planets.append(Planet(name, radius, mass, distance, ptype))

        elif choice == "3":
            name = input("Имя для удаления: ")
            found = False
            for p in planets:
                if p.name.lower() == name.lower():
                    planets.remove(p)
                    print(f"Планета {name} удалена")
                    found = True
                    break
            if not found:
                print("НЕт такой планеты")

        elif choice == "4":
            name = input("Имя планеты для редактирования: ")
            found = False
            for p in planets:
                if p.name.lower() == name.lower():
                    print(f"Редактируем {name}:")
                    p.name = input("Новое имя: ")
                    p.distance = float(input("Новое расстояние: "))
                    p.ptype = input("Новый тип: ")
                    p.radius = float(input("Новый радиус: "))
                    p.mass = float(input("Новая масса: "))
                    print("Обновлено")
                    found = True
                    break
            if not found:
                print("Нет такой планеты")
            
        elif choice == "5":
            f = input("Сортировать по (name/radius/mass/distance): ")
            bubble_sort(planets, f)
            print("Отсортировано")

        elif choice == "6":
            save(planets)
            print("Сохранено")
            break

if __name__ == "__main__":
    main()
