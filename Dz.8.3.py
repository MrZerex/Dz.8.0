class OnlyNum(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []

while True:
    elem = input('Введите элемент списка (целое число) - для выхода введите "stop": ')
    if elem == 'stop':
        print(my_list)
        break
    try:
        if elem.isdigit():
            my_list.append(int(elem))
        else:
            raise OnlyNum('Необходимо ввести целое число')
    except OnlyNum as onum:
        print(onum)
