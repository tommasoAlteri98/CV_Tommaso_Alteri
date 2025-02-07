def stringheInserite() :
    stringhe = []
    lunghezza_stringa = 0
    
    while True :
      stringaInserita = input("Inserisci una nuova stringa")
      if stringaInserita == "" :
          break
      
      if len(stringaInserita) >= lunghezza_stringa :
          lunghezza_stringa = len(stringaInserita)
          stringhe.append(stringaInserita)
          
      else :
          print("Stringa più corta: GIOCO FINITO!")
          break
    
    print ("Numero di stringhe inserite :" ,len(stringhe))
    print ("Elenco delle stringhe: ",stringhe)
    
stringheInserite()