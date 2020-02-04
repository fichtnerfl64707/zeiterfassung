
import eintrag

def main(): 
	while True: 
		print("""\
		Folgende Optionen stehen zur Verfügung:
		(1) Aktuelle Zeiterfassung ansehen.
		(2) Zeiteintrag hinzufügen.
		(3) Programm beenden.
			""")
		choice = int(input("Was möchtest du wählen? "))
		if choice == 1: 
			
			print("\nDie aktuelle Zeiterfassung wird geöffnet:\n")
			tabelle_ansehen()
		
		elif choice == 2: 
			print("\nNeuer Eintrag wurde gewählt\n")
			neuer_AT()
		elif choice == 3: 
			exit(0)
		else: 
			print("\nBitte nur Zahlen zwischen 1 und 3 eingeben!\n")


def tabelle_ansehen():

	tabelle = open("zeituebersicht.txt", "r+")
	print("Zeitübersicht geöffnet")
	if tabelle.read() == "" :

#		print("Uebersichts erste Zeile leer")
		tabelle.close()
		tabelle_erstellen(False,None)
	else: 
#		print("Vorhandene Übersicht anzeigen")
		tabelle.close()
		tabelle_anzeigen = open("zeituebersicht.txt", "r+")
		print(tabelle_anzeigen.read())

	
def tabelle_erstellen(status, Tabelle_AT): 
	Tabelle = ["Datum","Kommen","Gehen","Arbeitszeit","Differenz","Summe"]

	if status == False:
		print("Tabelle wird erstellt")
		tabelle_erstellen = open("zeituebersicht.txt", "r+")
		for spalte in Tabelle:
			tabelle_erstellen.write(spalte + " | ")
		
		tabelle_erstellen.write("\n")
		tabelle_erstellen.close()
		tabelle_ansehen()
	else: 
		tabelle_ergaenzen = open("zeituebersicht.txt", "a")
		for value in Tabelle_AT:
			tabelle_ergaenzen.write(str(value))
			tabelle_ergaenzen.write(" | ")
		#	print("Tabelle geschrieben")
		tabelle_ergaenzen.write("\n")
		tabelle_ergaenzen.close()
	


def neuer_AT():
	Tabelle_AT = ["datum", "kommen", "gehen","Arbeitszeit","Differenz","summe"]
	Tabelle_AT[0] = input("Bitte Datum eingeben: ")
	Tabelle_AT[1] = input("Bitte die Uhrzeit - Kommen eingeben: ")
	Tabelle_AT[2] = input("Bitte die Uhrzeit - Gehen eingeben: ")
	AT = eintrag(Tabelle_AT[0], Tabelle_AT[1], Tabelle_AT[2])
	Tabelle_AT[3] = AT.berechnen()
	Differenz = 7*60 - int(Tabelle_AT[3])
	Tabelle_AT[4] = str(Differenz)
	Tabelle_AT[5] = summe(Tabelle_AT)
	tabelle_erstellen(True, Tabelle_AT)
	
def summe(AT):
	data = open("zeituebersicht.txt","r")
	array_2d = []
	for line in data.readlines(): 
		array_2d.append(line.split(" | "))
	
	summe = int(AT[4])
	for zeile in array_2d: 
		if zeile[0] == "Datum": 
			continue
		summe = summe + int(zeile[4])
	summe = summe / 60
	return(str(summe))


if __name__ == '__main__':
	print("Das Zeiterfassungsprogrammm wurde gestartet!")
	main()





