class Animal:
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

class vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def muge(self):
        print(f'O{self.nome} a vaca muge')

class cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latindo(self):
        print(f'O{self.nome} o cachorro esta latindo')

    class gato(Animal):
        def __init__(self, nome, cor):
            super().__init__(nome, cor)

        def mia(self):
            print(f'O{self.nome} o gato mia')