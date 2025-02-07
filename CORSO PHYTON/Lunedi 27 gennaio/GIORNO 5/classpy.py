class Automobile:
    numero_di_ruote = 4
    def __init__(self, marca, modello) :
        self.marca = marca
        self.modello = modello
        
    def stampa__info(self):
        print(self.marca, self.modello)
    