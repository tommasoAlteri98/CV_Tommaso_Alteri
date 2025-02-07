primi = []

def primo_o_no(numero) :
    if numero < 2 : return False
    for i in range (2, int(numero ** 0.5) + 1) :
        if numero % i == 0:
            return False
    return True

while True : 
    nome = input("Inserisci il tuo nome o digita 'esci' per terminare il processo")
    if nome.lower() == "esci" :
        break
    
    numero = int(input("Inserisci il tuo numero"))
    