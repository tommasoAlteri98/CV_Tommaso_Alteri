import math

class Punto :
    x = 0
    y = 0
    
    def muoviPunti(self, new_x, new_y) :
        self.x = new_x
        self.y = new_y
        print("Nuove coordinate: " ,new_x ,new_y)
    
    def distanza_da_origine(self) :
        distanza = math.sqrt((self.x)**2 + (self.y)**2)
        print("La distanza tra il punto scelto e l'origine è: "  ,distanza)

p1 = Punto()
p1.muoviPunti(5, 6)
p1.distanza_da_origine()