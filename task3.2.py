sales = {
    "Понедельник": [("капучино", 120, 14), ("латте", 150, 9), ("чай", 60, 21)],
    "Вторник":     [("капучино", 120, 8),  ("эспрессо", 90, 17), ("чай", 60, 12)],
    "Среда":       [("латте", 150, 11), ("эспрессо", 90, 6), ("какао", 110, 13)],
    "Четверг":     [("капучино", 120, 16), ("латте", 150, 7), ("чай", 60, 18)],
    "Пятница":     [("капучино", 120, 10), ("эспрессо", 90, 21), ("какао", 110, 9)],
}
from math import*
def sum_day(day):
    total_day = 0
    for name,price,qty in sales[str(day)]:
        total_day += price * qty
    return total_day

print(sum_day('Понедельник') + sum_day('Вторник') + sum_day('Среда') + sum_day('Четверг') + sum_day('Пятница'))
print(max([sum_day('Понедельник'),'Понедельник'],[sum_day('Вторник'),'Вторник'],
          [sum_day('Среда'),'Среда'],[sum_day('Среда'),'Среда'],
          [sum_day('Пятница'),'Пятница'],))
print(((sum_day('Понедельник') + sum_day('Вторник') + sum_day('Среда') + sum_day('Четверг') + sum_day('Пятница'))/5)//1  )
def hit_day(day):
    best_day = ''
    cnt_day = 0
    for name,price,qty in sales[day]:
        if qty > cnt_day:
            cnt_pon = qty
            best_day = name
    return f'Хит {day} : {best_day}'