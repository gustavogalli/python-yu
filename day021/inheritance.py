class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale, exhale.')

# para HERDAR uma classe


class Fish(Animal):  # adicionamos a classe mãe dentro dos parâmetros
    def __init__(self):
        super().__init__()  # adicionamos isso para herdar os atributos

    def breathe(self):
        super().breathe()  # adicionamos isso para herdar os métodos que quisermos
        print('under water')

    def swim(self):
        print('moving in water')


nemo = Fish()
nemo.breathe()
