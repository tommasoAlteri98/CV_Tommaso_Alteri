from abc import ABC, abstractmethod

class Animale(ABC) :
    @abstractmethod
    def muovi(self) :
        pass

class Cane(Animale) :
    def muovi(self) :
        print("corro")

class Pesce(Animale) :
    def muovi(self) :
        print("nuoto")
        
pesce = Pesce()
cane = Cane()

cane.muovi()
pesce.muovi()
