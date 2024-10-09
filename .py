class Pessoa:
    def __init__ (self,nome,peso,idade,comendo=False,andando=False,dormindo=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade=0
        self.comendo=comendo
        self.andando=andando
        self.dormindo=dormindo

    def andar(self):
        if self.andando == False:
            print("foi andar")
            self.andando=True
        else:
            print("Já esta andando")

    def comer(self):
        if self.comendo == False:
            print("foi comer")
            self.comendo = True
        else:
            print("Já esta comendo")
    def dormir(self):
        if self.dormindo == False:
            print("foi dormir")
            self.dormindo=True
        else:
            print("Já esta dormindo")


p1 = Pessoa("Alexia",64,24)
p1.nome="Alexia Silva"
p1.dormir()
p1.dormir()

