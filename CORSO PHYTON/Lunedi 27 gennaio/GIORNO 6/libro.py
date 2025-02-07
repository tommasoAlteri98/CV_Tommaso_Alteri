class Libro : 
    def __init__(self, titolo, autore, pagine) :
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self) :
        pag = str(self.pagine)
        stri = "Il libro intitolato "+ self.titolo +" scritto da "+ self.autore+" è composto dal seguente numero di pagine: " +pag 
        return stri
        
libro1 = Libro("G.R.Martin", "Le Cronache del Ghiaccio e del Fuoco", 1569)
print(libro1.descrizione())