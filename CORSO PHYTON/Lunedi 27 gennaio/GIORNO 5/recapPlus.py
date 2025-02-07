import random

def chiedi_nome():
    return input("Inserisci il tuo nome")

def chiedi_riavvio():
    while True :
        risposta = input("Vuoi giocare un altra partita? SI o NO").lower()
        if risposta == "si" :
            return True
        elif risposta == "no" :
            return False
        else :
            print("ERRORE")
            
def chiedi_scelta_pari_dispari() :
    while True :
        scelta = input("Scegli pari o dispari").lower()
        if scelta =='pari' or scelta == 'dispari' :  
            return scelta
        else :
            print("Devi scrivere pari o dispari")
            
def chiedi_numero():
    while True :
        sceltaNumero = int(input("Inserisci un numero da 1 a 5"))
        if sceltaNumero < 1 or sceltaNumero >5 :
          print("Il numero deve essere un numero intero compreso tra 1 e 5")
        elif sceltaNumero >= 1 and sceltaNumero <= 5 :
          print("Hai scelto il tuo numero: " ,sceltaNumero)
        else :
          print("ERRORE NUMERICO")
          
def somma_numeri(*numeri) :
    return sum(numeri)

def gioca_partita() :
    sceltaNumero = chiedi_scelta_pari_dispari()
    numeroUtente = chiedi_numero()
    numeroCPU = random.randint(1, 5)
    print("Il computer ha scelto il numero: " ,numeroCPU)
    
    somma = somma_numeri(numeroUtente, numeroCPU)
    print("La somma delle due scelte è: " ,somma)
    
    if somma % 2 == 0 : 
        risultato = "pari" 
        print("Il totale è pari")
    else :
        risultato ="dispari"
        print("Il totale è dispari")
    if risultato == sceltaNumero :
        print("Hai vinto")
        return True
    else :
        print("Hai perso")
        return False
    
def aggiorna_punteggio(punteggio, partita_vinta) :
    vittorie, sconfitte = punteggio
    if partita_vinta :
        vittorie += 1
    else :
        sconfitte += 1
    return vittorie, sconfitte

def gioco() :
    print("Benvenuto nel gioco Pari o Dispari contro la CPU")
    punteggio = (0, 0)
    nomeUtente = chiedi_nome()
    
    while True :
        partita_vinta = gioca_partita()
        
        vittorie, sconfitte = aggiorna_punteggio(punteggio, partita_vinta)
        print("Vittorie: " ,vittorie)
        print("Sconfitte: " ,sconfitte)
        
        if not chiedi_riavvio() :
            print("Grazie per aver giocato, " ,nomeUtente)
            break
        punteggio = (0, 0)
    
if __name__ == "__main__" :
    gioco()