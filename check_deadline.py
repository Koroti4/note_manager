# gr_1_2_3
from datetime import date, datetime

# Запрос текущей даты
date_now = datetime.today().date()
date_now1 = date_now.strftime('%d.%m.%Y') # Перевод введенной даты в привычный мне формат дд.мм.гггг
print(f'Сегодня уже {date_now1}')

# Ввод даты и проверка корректности введенной даты
while True:
    date_deadline = input('Введите дату в формате дд.мм.гггг: ')
    try:
        datetime.strptime(date_deadline, '%d.%m.%Y').date()
        # print('Дата введена корректно')
        break
    except ValueError:
        print('Дата введена некорректно!')

# Перевод формата даты из дд.мм.гггг в формат datetime гггг-мм-дд
date_deadline = datetime.strptime(date_deadline, '%d.%m.%Y').date()

# Разница между текущей и введенной датой (.days - переводит в целочисленный тип)
date_interval = (date_deadline - date_now).days

if date_interval >= 1:
      print(f'До крайнего срока еще {date_interval} дней')
elif date_interval == 0:
     print(f'Сегодня уже нужно сдать это!')# date_note=strptime(dict_note_date, '%d.%m.%Y')
else:
     date_interval = date_interval * (-1)
     print(f'Это нужно было сделать {date_interval} дней назад')

