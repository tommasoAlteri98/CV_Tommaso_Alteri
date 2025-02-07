import random

nomeUtente = input("Inserisci il tuo nome")
print("Ciao " + nomeUtente + ", benvenuto nel gioco Pari o Dispari vs CPU")
vittorie = 0
sconfitte = 0

while True :
    pariOdispari = input("Scegli pari o scegli dispari?").lower()
    #if pariOdispari != "pari" or pariOdispari !="dispari" :
    while pariOdispari not in ["pari", "dispari"]:
        print("Scelta non valida")
        pariOdispari = input("Scegli Pari o Dispari").lower()
    sceltaNumero = int(input("Inserisci un numero da 1 a 5"))
    if sceltaNumero < 1 or sceltaNumero >5 :
        print("Il numero deve essere un numero intero compreso tra 1 e 5")
    elif sceltaNumero >= 1 and sceltaNumero <= 5 :
        print("Hai scelto il tuo numero: " ,sceltaNumero)
    else :
        print("ERRORE")
    
    numeroCPU = random.randint(1, 5)
    print("Il computer ha scelto il numero: " ,numeroCPU)
    
    somma = numeroCPU + sceltaNumero
    print("La somma delle due scelte è: " ,somma)
    
    if somma % 2 == 0 : 
         risultato = "pari" 
         print("Il totale è pari")
    else :
        risultato ="dispari"
        print("Il totale è dispari")
    
    if risultato == pariOdispari :
        print("Hai vinto")
        vittorie += 1
    else :
        print("Hai perso")
        sconfitte += 1
    print("Vittorie: " ,vittorie)
    print("Sconfitte: " ,sconfitte)
    
    continua = input("Vuoi continuare a giocare? Si o No").lower()
    if continua == "no" :
        print("Partita terminata!")
        vittorie=0
        sconfitte=0
        break