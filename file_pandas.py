import pandas as pd



# Facciamo le stesse operazioni che fatte nel file 'file_csv.py' ma utilizzando il modulo pandas, una libreria che ci semplifica molto la vita
# path: "C:/GEOGRAFIA E PROCESSI TERRITORIALI/SECONDO ANNO/LABORATORIO 2/Python/dati_pianosa_8-4-22/points_pianosa.csv"

my_csv = pd.read_csv('C:/GEOGRAFIA E PROCESSI TERRITORIALI/SECONDO ANNO/LABORATORIO 2/Python/dati_pianosa_8-4-22/points_pianosa.csv')  # Funzione che legge il csv

print(type(my_csv))
#print(my_csv)  # pandas non usa cicli per iterare sulle righe del file csv
#   accedendo alle colonne come un dizionario, posso eseguire script automatici per modificare i file
my_csv['coordx'] = my_csv['coordx']+100
print(my_csv['coordx']) # ho aumentato di 100 le coordx di tutte le righe
print(my_csv['luogo'])  # si vede che pandas assegna un suo id alle righe

# pandas, diversamente dal modulo csv, ha una sua tabella che è il DataFrame
print(type(my_csv))

# Le colonne del DF sono elementi chiamati Series
print(type(my_csv['coordx']))


''' tenere questa parte commentata se si devono solo fare operazioni senza creare un file...
my_csv.to_csv('C:/GEOGRAFIA E PROCESSI TERRITORIALI/SECONDO ANNO/LABORATORIO 2/Python/dati_pianosa_8-4-22/points_PANDAS_pianosa.csv')
print('Done!')'''

