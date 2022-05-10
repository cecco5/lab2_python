# SCRIPT PER LEGGERE E SCRIVERE FILE CSV

import csv

# path csv  C:/GEOGRAFIA E PROCESSI TERRITORIALI/SECONDO ANNO/LABORATORIO 2/Python/dati_pianosa_8-4-22/points_pianosa.csv
#my_csv = open("C:/GEOGRAFIA E PROCESSI TERRITORIALI/SECONDO ANNO/LABORATORIO 2/Python/dati_pianosa_8-4-22/points_pianosa.csv", 'r')

# print(my_csv) # stampando in questo modo non stampa i dati all'interno ma soltanto il textIOWrapper che è solo una codifica

# table = csv.reader(my_csv, delimiter=',')   # apro file csv con il metodo reader del modulo csv -> legge ogni riga come una lista
#table = csv.DictReader(my_csv, delimiter=',') # uguale ma legge ogni riga come un dizionario con chiavi e valori
'''
for row in table:   # tutti i valori vengono letti come stringhe, quindi spesso per fare operazioni vanno convertiti
    print(row["luogo"], row["xcoord"])    # posso così chiamare i valori delle chiavi specificate

for row in table:
    a = float(row["xcoord"])    # NB: RICORDARE SEMPRE DI CONVERTIRE I DATI PER MODIFICARLI, altrimenti sono letti come stringhe
    print(a + 200)
'''
# INSERIRE L'HEADER IN MODO AUTOMATICO AI FILE CSV

# praticamente dobbiamo aggiungere una lista all'inizio del file:
header = ["id","luogo","stato","xcoord","ycoord"]

my_csv = open("C:/GEOGRAFIA E PROCESSI TERRITORIALI/SECONDO ANNO/LABORATORIO 2/Python/dati_pianosa_8-4-22/points_pianosa.csv", 'r')
# utilizziamo reader e non Dictreader
table = csv.reader(my_csv, delimiter=',')

superlista = []    # lista di accumulo, conterrà tutte le righe del csv

for row in table:
    superlista.append(row)

#print(superlista)

#   ora per salvare tutto in un nuovo csv, creo un nuovo file (nome diverso dal precedente)
#   e ci appendo tutte le righe del csv con in capo l'header

new_csv = open("C:/GEOGRAFIA E PROCESSI TERRITORIALI/SECONDO ANNO/LABORATORIO 2/Python/dati_pianosa_8-4-22/points_pianosa_header.csv",'w')
new_table = csv.writer(new_csv, delimiter=',')  # apro il nuovo file come tabella

#   e ora inserisco l'header + tutte le righe del csv precedente (superlista)
new_table.writerow(header)
new_table.writerows(superlista)

#   chiudo tutti i file
my_csv.close()
new_csv.close()
print("Done!")

# LO SCRIPT FUNZIONA!





