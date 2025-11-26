"""
функция найти_период_дня(часы):
  если часы от 6 до 11:
    вернуть "утра"
  иначе если часы от 12 до 17:
    вернуть "дня"
  иначе если часы от 18 до 23:
    вернуть "вечера"
  иначе если часы от 0 до 5:
    вернуть "ночи"

функция склонение_часов(часы):
  если часы оканчиваются на 1 и часы не равны 11:
    вернуть часы + " час"
  иначе если часы оканчиваются на 2,3,4 и часы не в диапазоне 12-14:
    вернуть часы + " часа"
  иначе:
    вернуть часы + " часов"

функция склонение_минут(минуты):
  если минуты оканчиваются на 1 и минуты не равны 11:
    вернуть минуты + " минута"
  иначе если минуты оканчиваются на 2,3,4 и минуты не в диапазоне 12-14:
    вернуть минуты + " минуты"
  иначе:
    вернуть минуты + " минут"

функция преобразовать_время_в_текст(часы, минуты):
  если часы = 0 и минуты = 0:
    вернуть "полночь"
  если часы = 12 и минуты = 0:
    вернуть "полдень"
  
  период = найти_период_дня(часы)
  
  часы_в_12 = часы
  если часы = 0:
    часы_в_12 = 12
  иначе если часы > 12:
    часы_в_12 = часы - 12

  часы_текст = склонение_часов(часы_в_12)
  минуты_текст = склонение_минут(минуты)

  результат = часы_текст + " " + минуты_текст + " " + период
  если минуты = 0:
    результат = результат + " ровно"

  вернуть результат

основная программа:
  получить ввод от пользователя
  если ввод пустой:
    вывести ошибку
    завершить программу
  
  разделить ввод на две части
  если частей не две:
    вывести ошибку
    завершить программу

  часть1 = первая часть ввода
  часть2 = вторая часть ввода

  если часть1 не число или часть2 не число:
    вывести ошибку
    завершить программу

  часы = преобразовать часть1 в число
  минуты = преобразовать часть2 в число

  если часы < 0 или часы > 23:
    вывести ошибку
    завершить программу

  если минуты < 0 или минуты > 59:
    вывести ошибку
    завершить программу

  текст_времени = преобразовать_время_в_текст(часы, минуты)
  вывести текст_времени
"""

def get_day_period(hours):
    if hours >= 6 and hours < 12:
        return "утра"
    elif hours >= 12 and hours < 18:
        return "дня"
    elif hours >= 18 and hours < 24:
        return "вечера"
    elif hours >= 0 and hours < 6:
        return "ночи"

def hour_declination(hours):
    if hours % 10 == 1 and hours != 11:
        return str(hours) + " час"
    elif (hours % 10 >= 2 and hours % 10 <= 4) and not (hours >= 12 and hours <= 14):
        return str(hours) + " часа"
    else:
        return str(hours) + " часов"

def minute_declination(minutes):
    if minutes % 10 == 1 and minutes != 11:
        return str(minutes) + " минута"
    elif (minutes % 10 >= 2 and minutes % 10 <= 4) and not (minutes >= 12 and minutes <= 14):
        return str(minutes) + " минуты"
    else:
        return str(minutes) + " минут"

def correct_number(number):
    if number.isdigit():
        return True
    else:
        return False

def get_time_in_words(hours, minutes):
    if hours == 0 and minutes == 0:
        return "полночь"
    if hours == 12 and minutes == 0:
        return "полдень"

    period = get_day_period(hours)

    hours_in_12 = hours
    if hours == 0:
        hours_in_12 = 12
    elif hours > 12:
        hours_in_12 = hours - 12

    hours_in_12_in_words = hour_declination(hours_in_12)
    
    if minutes == 0:
        result = f"{hours_in_12_in_words} {period} ровно"
    else:
        minutes_in_words = minute_declination(minutes)
        result = f"{hours_in_12_in_words} {minutes_in_words} {period}"

    return result

def main():
    data_input = input("Введите время через пробел: ").strip()
    if not data_input:
        print("Ошибка: ничего не было введено.")
        return

    data_parts = data_input.split()
    if len(data_parts) != 2:
        print("Ошибка: требуется 2 целых числа через пробел.")
        return

    hours, minutes = data_parts

    if not (correct_number(hours) and correct_number(minutes)):
        print("Ошибка: некорректные символы. Введите 2 целых числа через пробел.")
        return

    hours, minutes = int(hours), int(minutes)

    if hours < 0 or hours > 23:
        print("Введены недопустимые данные: часы должны быть от 0 до 23.")
        return

    if minutes < 0 or minutes > 59:
        print("Введены недопустимые данные: минуты должны быть от 0 до 59.")
        return

    print(get_time_in_words(hours, minutes))

if __name__ == "__main__":
    main()