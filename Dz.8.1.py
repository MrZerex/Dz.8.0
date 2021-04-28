class Date:
    def __init__(self, dates):
        self.dates = dates

    @classmethod
    def str_date(cls, dates):
        try:
            dates = list(map(int, dates.split('-')))
            return print(f'Число - {dates[0]}, месяц - {dates[1]}, год - {dates[2]}')
        except (AttributeError, ValueError, IndexError):
            print('Некорректная запись')

    @staticmethod
    def valid_date(dates):
        try:
            dates = list(map(int, dates.split('-')))
            if (dates[0] > 32 or dates[0] < 0) or (0 > dates[1] or dates[1] > 12) or 0 > dates[2]:
                print('Некорректная дата (значение дней от 1 до 31, значение месяца'
                      ' от 1 до 12, год не может быть меньше 0)')
            else:
                print('Дата записана верно', dates[0])
        except (AttributeError, ValueError, IndexError):
            print('Некорректная запись')

while True:
    date = input('Введите строку формата "дд-мм-гггг" (целыми числами, для выхода введите N): ')
    if date == 'N':
        break
    a = Date(date)
    a.str_date(date)
    a.valid_date(date)




