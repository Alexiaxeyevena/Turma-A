class pessoa:
    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo=False
        self.andando=False
        self.dormindo=False

    def comer(self):
        if self.comendo==False:
            if self.andando==False:
                if self.dormindo==False:
                    print(f"{self.nome} foi comer")
                    self.comendo=True
                else:
                    print(f"{self.nome} não pode comer, pois está dormindo")

            else:print(f"{self.nome} não pode comer, pois está andando")

        else:print(f"{self.nome} já estava comendo")
    def dormir(self):
        if self.comendo==False:
            if self.andando==False:
                if self.dormindo==False:
                    print(f"{self.nome} foi comer")
                    self.comendo=True
                else:
                    print(f"{self.nome} não pode comer, pois está dormindo")

            else:print(f"{self.nome} não pode comer, pois está andando")

        else:print(f"{self.nome} já estava comendo")


p1 = pessoa("Alexia", 68, 24)
p1.nome = "Alexiaxeyevena"
p1.andar()
p1.comer()

class Animal:
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
        self.comendo=False

    def comer(self):
        print(f"{self.nome} está comneod")