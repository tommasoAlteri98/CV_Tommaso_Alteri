class Veicolo :
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def mostra_info(self):
        print("Marca: " + self.marca + ", Modello: " + self.modello)
        
class DotazioniSpeciali :
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
            
    def mostra_dotazioni(self):
        print(f"dotazioni speciali :{','.join(self.dotazioni)} ")
            
class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli) :
        Veicolo.__init__(self, marca, modello)
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli
        
    def mostra_info(self):
        super().mostra_info()
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()
        
auto1 = Veicolo("Fiat","Punto")
auto2 = AutomobileSportiva("Ferrari","Testarossa",["Cavallino d'oro","Sedili in pelle"],"2000")

auto1.mostra_info()
auto2.mostra_info()
