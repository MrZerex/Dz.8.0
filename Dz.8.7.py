class ComplexNum:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return ComplexNum(self.num + other.num)

    def __mul__(self, other):
        return ComplexNum(self.num * other.num)

    def __str__(self):
        return f'Результат вычислений: {self.num}'

num_1 = ComplexNum(complex(3, 4))
num_2 = ComplexNum(complex(6, 3))
num_3 = ComplexNum(complex(-3, -2))
print(num_1 + num_2)
print(num_1 * num_2)
print(num_1 + num_2 + num_3)
print(num_1 * num_2 * num_3)