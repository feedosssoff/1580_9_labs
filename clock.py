def get_day_period(hours):
  if hours >= 6 and hours <= 11:
    return "утра"
  elif hours >= 12 and hours <= 17:
    return "дня"
  elif hours >= 18 and hours <= 23:
    return "вечера"
  elif hours >= 0 and hours <= 5:
    return "ночи"

def hour_declination():
  if hours % 10 == 1 and hours != 11:
    return str(hours) + "час"
  elif (hours % 10 >= 2 and hours % 10 <= 4) and not (hours >= 12 and hours <= 14):
    return str(hours) + "часа"
  else:
    return str(hours) + "часов"

def minute_declination():
  if minutes % 10 == 1 and minutes != 11:
    return "минута"
  elif (minutes % 10 >= 2 and minutes % 10 <= 4) and not (minutes >= 10 and minutes < 20):
    return "минуты"
  else:
    return "минут"

def correct_number(number):
  numbers = "0123456789"
  for char in number:
    if chat not in numbers:
      return False
  return True

def get_time_in_words(hours, minutes):
  if hours == 0 and minutes == 0:
    return "полночь"
  if hours == 12 and minutes == 0:
    return "полдень"
  
  period = get_time_period(hours)

  hours_in_12 = hours
  if hours == 0:
    hours_in_12 = 12
  elif hours > 12:
    hours_in_12 = hours - 12

  hours_in_12_in_words = format_hours(hours_in_12)
  minutes_in_words = format_minutes(minutes)

  result = f"{hours_in_12_in_words} {minutes_in_words} {period}"
  if minutes == 0:
    result += " ровно"

  return result

def main():
  data_input = input("Введите время через пробел").strip()
  if not data_input:
    print("Ошибка: ничего не было введено.")
    return
    
  if len(data_input().split()) != 2:
    print("Ошибка: требуется 2 целых числа через пробел.")
    return

  hours, minutes = data_input().split()

  if not (correct_number(hours) and correct_number(minutes)):
    print("Ошибка некорректные символы. Введите 2 целых числа через пробел.")
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
