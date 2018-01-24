import os
import time

sciezka = input("Podaj pełną ścieżkę katalogu do przeskanowania: ")
print("\n\nKatalog przeskanowany\n")
print("Wynik:\n")

calaSciezka = []
for root, dirs, files in os.walk(sciezka):
    for file in files:	
    	try:
    		calaSciezka.append(str(root)+"/"+file)
    	except:
    		pass

Pliki = {}

for dirs in calaSciezka:
    Pliki[str(dirs)] = os.path.getsize(dirs)


def sortuj(dictio):
	while(dictio != {}): 
		maxi = 0
		key = ''
		for keys in dictio:
			if(dictio[keys] > maxi):
				maxi = dictio[keys]
				key = keys
		print(key + " waży " + str(dictio[key])+ " bajtów")
		del dictio[key]

sortuj(Pliki)
time.sleep(60)
