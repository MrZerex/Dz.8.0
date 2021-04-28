class NotZero(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        num_1 = int(input('Введите первое число: '))
        num_2 = int(input('Введите первое число: '))
        if num_2 == 0:
            raise NotZero('Нельзя делить на ноль')
        rez = num_1 / num_2
    except ValueError:
        print('Нужно ввести целое число')
    except NotZero as Zer:
        print(Zer)
    else:
        print(rez)
        break