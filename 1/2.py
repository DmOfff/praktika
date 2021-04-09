# Вывести на экран текущее название дня недели, название месяца и свое имя. Каждое слово должно быть в отдельной строке.

import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU')

weekDays = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

print(weekDays[datetime.datetime.now().weekday()])
print(calendar.month_name[datetime.datetime.now().month])
print("Дмитрий")