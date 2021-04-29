class SkladOrgTech:
    pp = 0
    ss = 0
    kk = 0
    printers_dict = {}
    scaners_dict = {}
    kserox_dict = {}
    in_printer = []
    in_scaner = []
    in_kserox = []

    @staticmethod
    def sklad(company, key):
        if key == 'П':
            SkladOrgTech.printers_dict[SkladOrgTech.pp] = company
            print(SkladOrgTech.printers_dict)
            print(f'Количество принтеров на складе: {SkladOrgTech.pp}')
        elif key == 'С':
            SkladOrgTech.scaners_dict[SkladOrgTech.ss] = company
            print(SkladOrgTech.scaners_dict)
            print(f'Количество сканеров на складе: {SkladOrgTech.ss}')
        elif key == 'К':
            SkladOrgTech.kserox_dict[SkladOrgTech.kk] = company
            print(SkladOrgTech.kserox_dict)
            print(f'Количество ксероксов на складе: {SkladOrgTech.kk}')
        elif key == 'N':
            SkladOrgTech.printers_dict.clear()
            SkladOrgTech.scaners_dict.clear()
            SkladOrgTech.kserox_dict.clear()
            SkladOrgTech.pp = 0
            SkladOrgTech.ss = 0
            SkladOrgTech.kk = 0

    @staticmethod
    def to_comp():
        print(f'В подразделения было отправлено: {SkladOrgTech.pp} принтеров, {SkladOrgTech.ss} сканеров,'
              f'{SkladOrgTech.kk} ксероксов')
        if SkladOrgTech.printers_dict:
            SkladOrgTech.in_printer.append(SkladOrgTech.printers_dict.copy())
        elif SkladOrgTech.scaners_dict:
            SkladOrgTech.in_scaner.append(SkladOrgTech.scaners_dict.copy())
        elif SkladOrgTech.kserox_dict:
            SkladOrgTech.in_kserox.append(SkladOrgTech.kserox_dict.copy())
        print(f'Список отправленных принтеров: {SkladOrgTech.in_printer}, список отправленных сканеров: {SkladOrgTech.in_scaner}, '
              f'список отправленных ксероксов {SkladOrgTech.in_kserox}')

class OrgTech(SkladOrgTech):

    def __init__(self, company):
        self.company = company

class Printer(OrgTech):

    def __init__(self, company, key):
        super().__init__(company)
        self.key = key
        SkladOrgTech.pp += 1


class Scaner(OrgTech):
    def __init__(self, company, key):
        super().__init__(company)
        self.key = key
        SkladOrgTech.ss += 1

class Kserox(OrgTech):
    def __init__(self, company, key):
        super().__init__(company)
        self.key = key
        SkladOrgTech.kk += 1


while True:
    while True:
        otech = input('Введите наименование техники (П - принтер, С - сканер, К - ксерокс),'
                      ' для отправки техники в подразделения введите "N": ')
        if otech == 'П':
            param_1 = input('Введите название компании производителя: ')
            prntr = Printer(param_1, otech)
            prntr.sklad(param_1, otech)
        elif otech == 'С':
            param_1 = input('Введите название компании производителя: ')
            scanr = Scaner(param_1, otech)
            scanr.sklad(param_1, otech)
        elif otech == 'К':
            param_1 = input('Введите название компании производителя: ')
            ksrx = Kserox(param_1, otech)
            ksrx.sklad(param_1, otech)
        elif otech == 'N':
            break
        else:
            print('Некорректное значение')
    if input('Для отмены действия введите "NN": ') == 'NN':
        continue
    SkladOrgTech.to_comp()
    non = SkladOrgTech()
    non.sklad(None, otech)
    ends = input('Для выхода из программы введите "N", для продолжения введите любое значение: ')
    if ends == 'N':
        break