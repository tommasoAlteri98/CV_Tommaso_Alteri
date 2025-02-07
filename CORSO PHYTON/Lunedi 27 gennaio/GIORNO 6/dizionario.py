lista = {}

while True :
    boleano = input("Inserisci un valore booleano").lower()
    if boleano == "true" :
        boleano = True
    elif boleano == "false" :
        boleano = False
    else :
        print("Valore booleano non riconosciuto! Riprova.")
        continue
    
    numero = int(input("Inserisci un numero"))
    stringa = input("Inserisci la tua stringa")
    
    dati_lista = [boleano, numero, stringa]
    lista['tipiDiDato'] = dati_lista
    
    print("Lista degli elementi del dizionario: " ,lista)
    
    break
    