class Animale :
    def __init__(self, nome) :
        self.nome = nome
    
    def parla(self) :
        print(self.nome + " fa suono genrrico")

class Cane(Animale) :
    def parla(self) :
        print(self.nome + " abbaia")
        
anomale_generico = Animale("Animale genrrico")
cane = Cane("Fido")

anomale_generico.parla()
cane.parla()