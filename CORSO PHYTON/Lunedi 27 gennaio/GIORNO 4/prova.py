def decoratore(funzione):
  def wrapper():
      print("Prima dell'esecuzione")
      funzione()
      print("dopo dell'esecuzione")
      
  return wrapper

@decoratore
def saluta():
    print("ciao")
    
saluta()