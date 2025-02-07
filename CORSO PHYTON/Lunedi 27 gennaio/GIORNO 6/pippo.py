studente = {
    "nome" : "Alice",
    "eta" : 29,
    "sesso" : "tanto",
    "altezza" : 176
}

studente["sesso"] = "poco"
studente["nome"] = "Pippo"
studente["altezza"] = 180
studente["eta"] = 22

print(studente)
print(studente.keys())
print(studente.values())
print(studente.get("regione"))