import json # moduł potrzebny do pracy z JSON-em

# 1. Otwieramy plik JSON do odczytu
with open('TestFiles/data.json', 'r') as file:
    myFile = json.load(file)

# 2. Dodajemy nowe pole do obiektu JSON
myFile["checked"] = True # po prostu dodajemy klucz tak jak w zwykłym słowniku

# 3. Zapisujemy zmienione dane z powrotem do pliku JSON
with open("TestFiles/data.json", "w") as file:
    json.dump(myFile, file, indent=4) # zapisujemy w ładnym formacie