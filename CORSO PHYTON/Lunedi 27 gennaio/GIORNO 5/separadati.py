def separazione(ripetizioni) :
    stringhe =[]
    floats = []
    interi = []
    
    for _ in range(ripetizioni) :
        inserisci = input("Inserisci un numero o una stringa")
        
        if inserisci.isdigit() or (inserisci.startswith('-') and inserisci[1:].isdigit()) :     #da riga 6 a riga 11 mi sono aiutato con chatgpt, penso però di aver capito
            interi.append(int(inserisci))                                                       # non sono però riuscito a far contare come float i numeri con la virgola
        elif inserisci.replace('.', '', 1).isdigit() and inserisci.count('.') == 1 :            # che vengono considerati string (col punto invece sono float)
            floats.append(inserisci)                                                            
        else :
            stringhe.append(inserisci)
    
    print("Lista delle stringhe" ,stringhe)
    print("Lista dei floats" ,floats)
    print("Lista degli interi" ,interi)
    
    sceltaStampa = input("Quale lista vuoi stampare? Interi, Floats, stringhe o tutte?").lower()
    
    if sceltaStampa == "stringhe" :
        print ("Lista stringhe:" ,stringhe)
    elif sceltaStampa == "floats" :
        print ("Lista floats:" ,floats)
    elif sceltaStampa == "interi" :
        print ("Lista interi:" ,interi)
    elif sceltaStampa == "tutte" :
        print ("Lista stringhe:" ,stringhe)
        print ("Lista floats:" ,floats)
        print ("Lista interi:" ,interi)
    else :
        print("Errore")
        
ripetizioni = int(input("Quante ripetizioni di tutto il ciclo vuoi fare?"))
separazione(ripetizioni)
        